-- cache image files associated to a type
local data = mw.loadData('Module:Socials/data') or {}
local format = require "Module:Format"

---@class Socials
---@field ICON_SIZE number
local p = {
    ICON_SIZE = 25,

    TEMPLATES = {
        ICON = {
            DEFAULT = "[[{icon}|{iconSize}px]]",
            WITH_LINK = "[[{icon}|link={link} |{iconSize}px]]",
        },
        NO_TEXT = {
            DEFAULT = "{text}",
            WITH_LINK = "[{link} {text}]",
            WITH_PAGE = "[[{page}]]",
        },
        TEXT = {
            DEFAULT = "{text}",
            WITH_LINK = "[{link} {text}]",
            WITH_PAGE = "[[{page}|{text}]]",
        },
    },
}

---Try to provide backward compatibility with old usage
---@TODO: replace every instances using the previous method with the new one, then remove this function
---@param frame frame
---@return string|nil
p._try_backward_compatibility = function(frame)
    local args = frame:getParent().args -- we check in the parent template params (aka Infobox/socials)
    local text = args["1"] or ""
    local type, link

    local arg_keys = { -- previously supported keys
        ["discord"] = true,
        ["steam"] = true,
        ["github"] = true,
        ["bitbucket"] = true,
        ["X"] = true,
        ["forum"] = true,
        ["blog"] = true,
        ["gdrive"] = true,
        ["npmjs"] = true,
    }

    -- check if any of the old keys is provided
    for k, v in pairs(args) do
        if arg_keys[k] then
            type = k
            link = v
            break
        end
    end

    -- handle other and custom cases
    if not type then
        local other = args["other"]
        local custom = args["custom"]
        if other then
            link = other
        elseif custom then
            text = custom
        else
            return
        end

        type = "default"
    end

    -- handle nolink case
    if link and link == "nolink" then
        link = nil
    end

    -- retrieve icon
    local icon_link = p._get_icon_link(type)

    -- remove spaces at the start and end
    text = mw.text.trim(text)
    if text == "" then
        -- in this scenario, it's likely a custom link without a provided text,
        -- such as in one of the examples (direct blog link)
        ---@cast link string
        text = link
        link = nil
    end

    ---@FIXME: adjust to new TEMPLATES structure
    local template_id = link and "WITH_LINK" or "DEFAULT"
    local template_icon = p.TEMPLATES.ICON[template_id]
    local template_text = p.TEMPLATES.TEXT[template_id]

    local params = {
        icon = icon_link,
        iconSize = tostring(p.ICON_SIZE),
        text = text,
    }
    params.link = link

    local out_icon = p._format_template(template_icon, params)
    local out_text = p._format_template(template_text, params)
    return out_icon .. "\n" .. out_text
end

---Retrieve the icon from provided type, or return `default`.
---@TODO: improve feedback for provided type not existing
---@param t string
---@return string
p._get_icon_link = function(t)
    t = t ~= "" and t
        or "default" -- no icon nor type provided

    return data[t]
        or data["default"] -- provided type doesn't exists
end

p._format_param = function(param)
    local s = mw.text.trim(tostring(param or ""))
    if s == "" then return nil end
    return s
end

p._format_template = function(template, params)
    return format._format_string(template, params)
end

---comment
---@param frame frame
p.socials = function(frame)
    local args = frame.args

    local out = p._try_backward_compatibility(frame)
    if out then return out end

    -- retrieve icon
    local _icon_arg = p._format_param(args["icon"])
    local icon_link = _icon_arg
        or p._get_icon_link(args["type"])

    -- retrieve the text, remove spaces at the start and end
    local text = p._format_param(args["1"]) or "link"

    local params = {
        icon = icon_link,
        iconSize = tostring(p.ICON_SIZE),
        text = text,
    }
    local link = p._format_param(args["link"])
    local page = p._format_param(args["page"])
    params.link = link
    params.page = page

    local template_icon_id = link and "WITH_LINK"
        or "DEFAULT"
    local template_text_id = link and "WITH_LINK"
        or page and "WITH_PAGE"
        or "DEFAULT"

    local template_icon = p.TEMPLATES.ICON[template_icon_id]
    local template_text = text == "link" and p.TEMPLATES.NO_TEXT[template_text_id]
        or p.TEMPLATES.TEXT[template_text_id]

    local out_icon = p._format_template(template_icon, params)
    local out_text = p._format_template(template_text, params)

    return out_icon .. " " .. out_text
end

return p
local data = mw.loadData('Module:JavaObject/data') or {}

local p = {}

---Main function to be called from wikitext.
---@param frame frame
p.javaObject = function(frame)
    local args = frame.args

    local object = args.object
    assert(object, "No object provided")

    local package = args.package
    assert(package, "No package provided")

    local doc = args.doc
    local docLink = (doc and data[doc] or data["default"]).link

    local link = docLink .. package .. "/" .. object .. ".html"

    return "[" .. link .. " " .. object .. "]"
end

return p
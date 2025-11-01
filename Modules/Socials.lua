-- cache image files associated to a type
local data = mw.loadData('Module:Socials/data') or {}

local p = {}

---comment
---@param frame frame
p.socials = function(frame)
    local args = frame.args

    local type = args["type"] -- mandatory param
    local file = data[type]
    if not file then
        
    end

end

return p
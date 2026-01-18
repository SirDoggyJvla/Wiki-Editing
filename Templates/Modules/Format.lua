local p = {}

---Format a string with given parameters
---@param s string
---@param params table
---@return string formated_string
---@return number count -- can be safely ignored
p._format_string = function(s, params)
    return s:gsub("{([%w_]+)}", params)
end

---Function for direct invoke
---@param frame frame
---@return string
p.format = function(frame)
    local args = frame.args
    local s = args[1] -- first arg is the string to format
    local params = {} -- every other params
    for k, v in pairs(args) do
        if k ~= "1" then
            params[k] = v
        end
    end

    local formated_string = p._format_string(s, params)
    return formated_string
end

return p

local p = {}

---@DEBUG
local function printTable(tbl, maxLvl, _lvl)
    if type(tbl) ~= "table" then mw.log("not a table: " .. tostring(tbl)) return end
    _lvl = _lvl or 0
    maxLvl = maxLvl or 2
    for k, v in pairs(tbl) do
        mw.log(string.rep(" ", _lvl * 4) .. tostring(k) .. " " .. tostring(v))
        -- DebugLog.log(tostring(k))
        if type(v) == "table" and _lvl < maxLvl then
            printTable(v, maxLvl, _lvl + 1)
        end
    end
end

---List pages in category
---@param frame frame
---@return string
p.list = function(frame)
    local args = frame.args
    local pages = {"test", "example", "sample"}
    local test = table.concat(pages, ", ")

    local namespace = mw.site.namespaces["Category"]
    -- local pages = mw.site.stats.pagesInCategory("Modding", "all")

    local title = mw.title.new("Category:Modding"):getContent()

    printTable(title, 0)

    -- printTable(namespace)
    -- for k,v in pairs(mw.site.namespaces) do
    --     test = tostring(k) .. ", " .. tostring(v)
    --     mw.log(test)
    -- end

    -- test = table.concat(mw.site.namespaces, ", ")

    return test
end

return p

--[[
DEBUG CONSOLE TESTS:
=p.list(
   mw.getCurrentFrame():newChild{
      title="Module:ListCategories",
      args={["category"]="TestCategory"}
   }
)
]]
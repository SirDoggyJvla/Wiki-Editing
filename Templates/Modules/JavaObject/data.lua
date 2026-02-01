---Make sure the links end with a /
---@type table<string, {link: string}>
local javaDocs = {
    ["official_B41"] = {link="https://projectzomboid.com/modding/"},
    ["unofficial_B41"] = {link="https://zomboid-javadoc.com/41.78/"},
    ["unofficial_B42"] = {link="https://demiurgequantified.github.io/ProjectZomboidJavaDocs/"},
}

-- most up-to-date Java doc
javaDocs["default"] = javaDocs["unofficial_B42"]

-- most trending / up-to-date docs for each versions
javaDocs["B41"] = javaDocs["unofficial_B41"]
javaDocs["B42"] = javaDocs["unofficial_B42"]

return javaDocs
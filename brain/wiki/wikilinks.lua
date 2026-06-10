-- wikilinks.lua
-- Converts Obsidian [[WikiLinks]] or [[WikiLinks|Display Text]] into relative markdown links

function Link (el)
  -- Catch standard markdown links that were written inside [[ ]]
  if el.target:match("^%%5B%%5B") or el.target:match("^%[%[") then
    -- Clean up URL-encoded or raw brackets
    local raw_target = el.target:gsub("^%%5B%%5B", ""):gsub("%%5D%%5D$", ""):gsub("^%[%[", ""):gsub("%]%]$", "")
    
    -- Handle alternative pipe text displays [[TargetNode|Display Text]]
    local path = raw_target
    local display = el.content
    
    if raw_target:find("|") then
      path = raw_target:match("^(.-)|")
      local txt = raw_target:match("|(.-)$")
      display = {pandoc.Str(txt)}
    end
    
    -- Normalize spacing to create matching lowercase, hyphenated filenames
    path = path:gsub("%s+", "-"):lower() .. ".md"
    
    return pandoc.Link(display, path)
  end
  return el
end

-- Catch raw unparsed bracket text instances 
function Str (el)
  if el.text:match("^%[%[") or el.text:match("%]%]$") then
    -- Clean up structural edge brackets hanging outside AST link objects
    el.text = el.text:gsub("%[%[", ""):gsub("%]%]", "")
    return el
  end
  return el
end
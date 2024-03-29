function euclideanDistance(x1, y1, x2, y2)
    local dist = math.sqrt((y2 - y1)^2 + (x2-x1)^2)
    return dist
end

function randomizeLocation(cx, cy, radius)
    while 1 do
        local x = love.math.random(cx-radius, cx+radius)
        local y = love.math.random(cy+radius, cy-radius)
        print(x)
        print(y)
        if (euclideanDistance(x, y, environment_center[1], environment_center[2]) < environment_radius-50) then
            return {x, y}
        end
    end
end

function allocateFood(n)
    food_locations = {}
    for i = 1, n do
        table.insert(food_locations, randomizeLocation(environment_center[1], environment_center[2], environment_radius))
    end
    return food_locations
end

function love.load()
    love.window.setMode(1000, 800)
    environment_center = {500, 400}
    environment_radius = 300
    food_image = love.graphics.newImage('resources/mushroom.png')
end

-- function love.update(dt)
--
-- end

function love.draw()
    love.graphics.setColor(1, 1, 1)
    love.graphics.circle('fill', environment_center[1], environment_center[2], environment_radius)
    for key, value in ipairs(allocateFood(20)) do
        love.graphics.draw(food_image, value[1], value[2])
    end
    love.timer.sleep(1)
end

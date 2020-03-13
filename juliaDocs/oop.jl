# THERE IS NO SUCH THING AS OOP IN JULIA
# you can make structs, but those are basically just 
# glorified jsons/dictionaries (imo)

struct Animal
    name::String
    food::String
    age::Int64
    function Animal(name, food, age)
        new(name, food, age)
    end
end

cow = Animal("mr. cow", "dog food", 21)


cow.blah()


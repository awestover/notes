using Test
@testset "first test" begin
    @test roman_to_dec("1") == "I"
end
@testset "second test" begin
    @test roman_to_dec("2") == "II"
end

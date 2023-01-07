"""
Julia 1.0で単位付き数値の算術 - Unitful パッケージ
https://qiita.com/tenfu2tea/items/882f539a9cf3cde1fa57
"""

using Unitful

v₀ = 13u"m/s"  # Initial velocity
t = LinRange(0, 2, 50) * u"s"  # Time range

v = v₀ .- 1u"gn" * t  # Velocity in vertical direction
y = v₀ * t .- 1u"gn" * t.^2/2  # Distance in vertical direction


# Unit conversion
t = t .|> u"ms"
v = v .|> u"mm/s"
y = y .|> u"mm"

# Plot
using Plots

p = plot(
    ustrip.(t),
    ustrip.(v),
    label = "velocity"
)


"""
p = plot(
    ustrip.(t),
    ustrip.(y),
    label = "Distance"
)
"""

display(p)

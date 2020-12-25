def determine_dangerous_allergen_ingredient_pairs(ingredients_per_allergen):
    dangerous_allergen_ingredient_pairs = [
        (allergen, mixture.pop())
        for allergen, mixture in ingredients_per_allergen.items()
        if len(mixture) == 1
    ]
    if dangerous_allergen_ingredient_pairs:
        dangerous_ingredients = {
            ingredient for _, ingredient in dangerous_allergen_ingredient_pairs
        }
        for mixture in ingredients_per_allergen.values():
            mixture -= dangerous_ingredients
        return (
            dangerous_allergen_ingredient_pairs
            + determine_dangerous_allergen_ingredient_pairs(ingredients_per_allergen)
        )
    return []


def solution(input_rel_uri):
    with open(input_rel_uri) as ifile:
        declarations = ifile.readlines()
    all_ingredients = []
    ingredients_per_allergen = {}
    for declaration in declarations:
        declaration = declaration.rstrip(")\n")
        ingredients_listing, _, allergens_listing = declaration.partition(" (contains ")
        ingredients = ingredients_listing.split()
        all_ingredients += ingredients
        if allergens_listing:
            allergens = allergens_listing.split(", ")
            for allergen in allergens:
                if allergen not in ingredients_per_allergen:
                    ingredients_per_allergen[allergen] = set(ingredients)
                else:
                    ingredients_per_allergen[allergen] &= set(ingredients)
    dangerous_allergen_ingredient_pairs = determine_dangerous_allergen_ingredient_pairs(
        ingredients_per_allergen
    )
    dangerous_allergen_ingredient_pairs.sort(key=lambda x: x[0])
    return ",".join(ingredient for _, ingredient in dangerous_allergen_ingredient_pairs)


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))

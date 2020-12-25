def determine_dangerous_ingredients(dangerous_mixtures_of_ingredients):
    newly_determined_dangerous_ingredients = {
        mixture.pop()
        for mixture in dangerous_mixtures_of_ingredients
        if len(mixture) == 1
    }
    if newly_determined_dangerous_ingredients:
        for mixture in dangerous_mixtures_of_ingredients:
            mixture -= newly_determined_dangerous_ingredients
        return newly_determined_dangerous_ingredients.union(
            determine_dangerous_ingredients(dangerous_mixtures_of_ingredients)
        )
    return set()


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
    dangerous_ingredients = determine_dangerous_ingredients(
        ingredients_per_allergen.values()
    )
    return sum(
        ingredient not in dangerous_ingredients for ingredient in all_ingredients
    )


if __name__ == "__main__":
    print(solution(f"../input/{__file__[-16:][:6]}.txt"))

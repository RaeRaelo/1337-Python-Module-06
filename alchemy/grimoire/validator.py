def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ['fire', 'water', 'earth', 'air']
    if any(ing in ingredients for ing in valid_ingredients):
        return (f"{ingredients} - VALID")
    else:
        return (f"{ingredients} - INVALID")

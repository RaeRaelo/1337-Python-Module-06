from alchemy.grimoire.spellbook import record_spell
from alchemy.grimoire.validator import validate_ingredients

print("=== Circular Curse Breaker ===")
print("\nTesting ingredient validation:")
print(f"validate_ingredients('fire air'): {validate_ingredients("fire air")}")
print("validate_ingredients('dragon scales'):"
      f"{validate_ingredients("dragon scales")}")

print("\nTesting spell recording with validation and late import:")
print('record_spell("Fireball", "fire air"):',
      record_spell("Fireball", "fire air"))
print('record_spell("Dark Magic", "shadow"):',
      record_spell("Dark Magic", "shadow"))
print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely")

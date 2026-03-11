from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import elixir_of_life, philosphers_stone
import alchemy.transmutation

print("=== Pathway Debate Mastery ===")
print("\nTesting Absolute Imports (from basic.py):")
print("lead_to_gold():", lead_to_gold())
print("stone_to_gem():", stone_to_gem())

print("\nTesting Relative Imports (from advanced.py)")
print("philosopher_stone():", philosphers_stone())
print("elixir_of_life():", elixir_of_life())

print("\nTesting Package Access:")
print("alchemy.transmutation.lead_to_gold():",
      alchemy.transmutation.lead_to_gold())
print("alchemy.transmutation.philosophers_stone():",
      alchemy.transmutation.philosphers_stone())
print("\nBoth pathways work! Absolute: clear, Relative: cocise")

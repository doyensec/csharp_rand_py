# C# Random Exploitation Library

This is an alternative, most mostly equivalent, re-implementation of C#'s
`Random::Next`.

This works by keeping everything in equations of the form `a * Seed + b mod p`.

You can `ressolve` these equations for any `Seed` to get the output of some
`(new Random(Seed).Next...)`.

You can do algebra on the equations to find other more complicated situations.

The equations can be copied to other languages easily. Just ensure you use 64
bit math. Using a 32 bit int will likely overflow and be in congruent mod
`2**31 - 1`.

# Examples

Get the equation that will represent the first output of `Random::Next` for any `Seed`.

```
>>> from csharp_rand import csharp_rand
>>> cs = csharp_rand()
>>> first = cs.sample_equation(0)
>>> print(first)
rand = seed * 1121899819 + 1559595546 mod 2147483647
```

Then running `.resolve(42)` will correspond to the output of 
`(new Random(42)).Next()`.

```
>>> first.resolve(42)
1434747710
```

Or you can use `.invert()` to go backwards, giving you the `Seed`.

```
>>> first.invert().resolve(1434747710)
42
```

More complicated, obtain the 726th output of `Random` from the 725th.

```
>>> late = 724
>>> late_rand = cs.sample_equation(late)
>>> late_rand_plus = cs.sample_equation(late + 1)
>>> late_to_late_plus = late_rand_plus(late_rand.invert())
>>> # check for seed 42
>>> late_to_late_plus.resolve(late_rand.resolve(42)) == late_rand_plus.resolve((42))
True
>>> print(late_to_late_plus)
rand = seed * 1971396503 + 1990619591 mod 2147483647
```

So `late_rand` represents the output of calling `.Next` 725 times. Then
`late_rand_plus` is 726. Since both of these have the same `Seed` in common, we
can invert `late_rand` and compose with `late_rand_plus` to get the equation
for going from the 725th `.Next` to 726th `.Next`.

We can check this by copying the `late_to_late_plus` and `late_rand.invert()`
equations to a .NET [playground](https://dotnetfiddle.net/PLLcyC).

```cs
using System;
					
public class Program
{

	// next two equations take from python csharp library
	private static int check(long seed) {
		long ret = (seed * 1971396503 + 1990619591) % 2147483647;
		return (int)ret;
	}

	private static int invert(long rand) {
		long ret = (rand * 1433598513 + 1157387419) % 2147483647;
		return (int)ret;
	}

	private static bool test(int Seed) {
		Console.WriteLine("Testing Seed {0}: ", Seed);
		var late = 724;
		var prng = new Random(Seed);
		for (int i = 0; i < late; i++) {
			prng.Next();
		}

		var first = prng.Next();
		var second = prng.Next();
		var c = check(first);

		Console.WriteLine("  Random[{0}]: {1}", late, first);
		Console.WriteLine("  Random[{0}]: {1}", late + 1, second);
		Console.WriteLine("  Computed:    {0}", c);
		Console.WriteLine("  Computed seed: {0}", invert(first));

		if (c == second) {
			Console.WriteLine("  Success");
			return true;
		}
		Console.WriteLine("  Failed");
		return false;
	}

	public static void Main() {
		for (int i = 278; i < 291; i++) {
			test(i);
		}
	}
}
```

Outputs:

```
Testing Seed 278: 
  Random[724]: 1558502570
  Random[725]: 827201365
  Computed:    827201365
  Computed seed: 278
  Success
Testing Seed 279: 
  Random[724]: 1583339083
  Random[725]: 1435417286
  Computed:    1435417286
  Computed seed: 279
  Success
...
```

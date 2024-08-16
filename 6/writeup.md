# 2023 Day 6

Let's start off with the equation for how far the boat goes given time $t$ and being held down for $h$.

$$
\begin{align*}
D(t, h) &= \text{velocity} \times \text{time moving} \\
&= h \times \text{time moving} \\
&= h \times (t - h) \\
&= th - h^2
\end{align*}
$$

With this equation, we can either iterate or try to come to an analytical solution.

## Iterative Solution

For iteration, we could either just do a linear search over the whole thing, linear search from each end until we find a winner, or binary search in both directions to the first winner from each direction.

## Analytical Solution

Let's just take a quick look at the analytical solution, where $r$ is the record distance.
Our known values are $r$ and $t$, and we're trying to find a range for $h$, with which we can get our count $c$.

$$
\begin{align*}
r &< D(t, h) \\
r &< th - h^2 \\
0 &< -r + th - h^2
\end{align*}\\
\text{From here we apply the quadratic formula.}\\
\begin{align*}
0 &= ax^2 + bx + c \\
x &= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\\
h &= \frac{-t \pm \sqrt{t^2 - 4r}}{-2}\\
h &= \frac{t \pm \sqrt{t^2 - 4r}}{2}\\
\end{align*}\\
\frac{t - \sqrt{t^2 - 4r}}{2} < h < \frac{t + \sqrt{t^2 - 4r}}{2}\\
\text{Bringing this back to integer land}\dots\\
\left\lceil\frac{t - \sqrt{t^2 - 4r}}{2}\right\rceil \leq h \leq \left\lfloor\frac{t + \sqrt{t^2 - 4r}}{2}\right\rfloor\\
c = \max(0, \lceil rhs \rceil - \lfloor lhs \rfloor - 1)
$$

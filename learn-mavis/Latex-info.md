# LaTeX Math for Undergraduates

<div align="left">
   <img alt="mavis" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-icon-banner-3.svg">
   <img alt="mavis-launcher" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-launcher-icon-banner-3.svg">
   <img alt="mavis-terminal" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/MAVIS-terminal-icon-banner-3.svg">
   <img alt="tg-loerrach" src="https://img.shields.io/badge/TG Lörrach-red?style=flat">
   <img alt="peharge" src="https://github.com/Peharge/MAVIS-images/blob/main/mavis-img-main/Peharge-icon-banner-3.svg">
</div>

## General Rules
- Any mathematical content, even a single character, should be written in a mathematical setting.
- Example: "the value of x is 7" should be written as `the value of $x$ is $7$`.

## Basic LaTeX Template
```latex
\documentclass{article}
\usepackage{mathtools, amssymb, amsthm, mathrsfs, bm} % imports essential math packages

\begin{document}
--document body here--
\end{document}
```

## Common Constructs
- Exponents: `x^2` → $x^2$
- Square Roots: `\sqrt{2}`, `\sqrt[n]{3}` → $\sqrt{2}$, $\sqrt[n]{3}$
- Subscripts: `x_{i,j}` → $x_{i,j}$
- Fractions: `\frac{2}{3}` → $\frac{2}{3}$
- Binomial Coefficients: `\binom{n}{k}` → $\binom{n}{k}$

## Calligraphic and Script Letters
- Calligraphic letters: `\mathcal{A}` → $\mathcal{A}$
- Script letters: `\mathscr{P}` (requires `\usepackage{mathrsfs}` in preamble)
- Bold Math Symbols: `\bm{x}` → $\bm{x}$

## Greek Letters

- `\alpha` → $ \alpha $
- `\beta` → $ \beta $
- `\gamma` → $ \gamma $
- `\delta` → $ \delta $
- `\epsilon` → $ \epsilon $
- `\zeta` → $ \zeta $
- `\eta` → $ \eta $
- `\theta` → $ \theta $
- `\iota` → $ \iota $
- `\kappa` → $ \kappa $
- `\lambda` → $ \lambda $
- `\mu` → $ \mu $
- `\nu` → $ \nu $
- `\xi` → $ \xi $
- `\omicron` → $ \omicron $
- `\pi` → $ \pi $
- `\rho` → $ \rho $
- `\sigma` → $ \sigma $
- `\tau` → $ \tau $
- `\upsilon` → $ \upsilon $
- `\phi` → $ \phi $
- `\chi` → $ \chi $
- `\psi` → $ \psi $
- `\omega` → $ \omega $

### Uppercase Greek Letters

- `\Gamma` → $ \Gamma $
- `\Delta` → $ \Delta $
- `\Theta` → $ \Theta $
- `\Lambda` → $ \Lambda $
- `\Xi` → $ \Xi $
- `\Pi` → $ \Pi $
- `\Sigma` → $ \Sigma $
- `\Upsilon` → $ \Upsilon $
- `\Phi` → $ \Phi $
- `\Psi` → $ \Psi $
- `\Omega` → $ \Omega $

## Sets and Logic Symbols

- `\cup` → $ \cup $
- `\cap` → $ \cap $
- `\subset` → $ \subset $
- `\subseteq` → $ \subseteq $
- `\supset` → $ \supset $
- `\supseteq` → $ \supseteq $
- `\in` → $ \in $
- `\notin` → $ \notin $
- `\emptyset` → $ \emptyset $
- `\mathbb{R}` → $ \mathbb{R} $
- `\mathbb{Z}` → $ \mathbb{Z} $
- `\mathbb{Q}` → $ \mathbb{Q} $
- `\mathbb{N}` → $ \mathbb{N} $
- `\mathbb{C}` → $ \mathbb{C} $
- `\forall` → $ \forall $
- `\exists` → $ \exists $
- `\neg` → $ \neg $
- `\vee` → $ \vee $
- `\wedge` → $ \wedge $
- `\vdash` → $ \vdash $
- `\models` → $ \models $
- `\setminus` → $ \setminus $
- `\complement` → $ \complement $

## Operators and Decorations
- Prime: `f'` → $f'$  
- Dots: `\ldots`, `\cdots`, `\vdots`, `\ddots`  
- Vectors: `\vec{x}`, `\boldsymbol{x}`  
- Derivatives: `\frac{d}{dx}f(x)` → $\frac{d}{dx}f(x)$  

## Functions and Roman Names

- `\sin` → $ \sin $
- `\cos` → $ \cos $
- `\tan` → $ \tan $
- `\arcsin` → $ \arcsin $
- `\arccos` → $ \arccos $
- `\arctan` → $ \arctan $
- `\sec` → $ \sec $
- `\csc` → $ \csc $
- `\cot` → $ \cot $
- `\exp` → $ \exp $
- `\log` → $ \log $
- `\ln` → $ \ln $
- `\det` → $ \det $
- `\dim` → $ \dim $
- `\gcd` → $ \gcd $
- `\lcm` → $ \lcm $
- `\lim` → $ \lim $
- `\sup` → $ \sup $
- `\inf` → $ \inf $
- `\ker` → $ \ker $
- `\arg` → $ \arg $
- `\deg` → $ \deg $

## Common Mathematical Symbols

- `<`, `>` → $ <, > $
- `\leq`, `\geq` → $ \leq, \geq $
- `\approx`, `\equiv`, `\cong`, `\sim`, `\simeq` → $ \approx, \equiv, \cong, \sim, \simeq $
- `\not=` → $ \not= $
- `\pm`, `\mp` → $ \pm, \mp $
- `\times`, `\div`, `\ast` → $ \times, \div, \ast $
- `\mid`, `\nmid` → $ \mid, \nmid $
- `\circ`, `\nabla`, `\partial` → $ \circ, \nabla, \partial $
- `\propto` → $ \propto $
- `\oplus`, `\otimes`, `\oslash` → $ \oplus, \otimes, \oslash $

## Arrows

- `\rightarrow`, `\to`, `\mapsto`, `\longrightarrow` → $ \rightarrow, \to, \mapsto, \longrightarrow $
- `\Leftarrow`, `\Rightarrow`, `\Leftrightarrow` → $ \Leftarrow, \Rightarrow, \Leftrightarrow $
- `\uparrow`, `\downarrow`, `\leftrightarrow`, `\updownarrow` → $ \uparrow, \downarrow, \leftrightarrow, \updownarrow $
- `\nrightarrow`, `\nRightarrow` → $ \nrightarrow, \nRightarrow $

## Summation and Integration
```
\sum_{j=0}^3 j^2
\int_{x=0}^3 x^2 \,dx
\iint \iiint \oint \bigcup \bigcap
```

$$
\sum_{j=0}^3 j^2
$$

$$
\int_{x=0}^3 x^2 \,dx
$$

$$
\iint \iiint \oint \bigcup \bigcap
$$

## Matrices and Arrays
```latex
\begin{pmatrix} a & b \\ c & d \end{pmatrix}
\begin{cases} a & \text{if } n=0 \\ r \cdot f_{n-1} & \text{else} \end{cases}
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
```

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$

$$
\begin{cases} a & \text{if } n=0 \\ r \cdot f_{n-1} & \text{else} \end{cases}
$$

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$

## Spacing in Mathematics

- `\,` → $ \, $
- `\: ` → $ \: $
- `\;` → $ \; $
- `\quad` → $ \quad $
- `\qquad` → $ \qquad $
- `\hspace{1cm}` → $ \hspace{1cm} $

## Displayed Equations
```latex
\begin{equation*} S = k \cdot \lg W \end{equation*}
\begin{align*} \nabla \cdot \boldsymbol{D} &= \rho \\ \nabla \cdot \boldsymbol{B} &= 0 \end{align*}
```

## Calculus Examples
```latex
\lim_{h\to 0} \frac{f(x+h)-f(x)}{h}
\int x^2 \,dx = \frac{x^3}{3} + C
\frac{\partial f}{\partial x} \quad \frac{\delta S}{\delta x}
```

$$
\lim_{h\to 0} \frac{f(x+h)-f(x)}{h}
$$

$$
\int x^2 \,dx = \frac{x^3}{3} + C
$$

$$
\frac{\partial f}{\partial x} \quad \frac{\delta S}{\delta x}
$$

## Discrete Mathematics Examples
```latex
\binom{n}{k} \quad n^{\underline{r}}
\sum_{k=0}^{n} k^2
```

$$
\binom{n}{k} \quad n^{\underline{r}}
$$

$$
\sum_{k=0}^{n} k^2
$$

## Statistics Examples
```latex
\sigma^2 = \sqrt{\sum (x_i - \mu)^2/N}
E(X) = \mu_X = \sum (x_i P(x_i))
\operatorname{Var}(X) = E(X^2) - (E(X))^2
```

$$
\sigma^2 = \sqrt{\sum (x_i - \mu)^2/N}
$$

$$
E(X) = \mu_X = \sum (x_i P(x_i))
$$

$$
\operatorname{Var}(X) = E(X^2) - (E(X))^2
$$

## Advanced LaTeX Formula Collection

### Matrices and Determinants
```latex
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc

\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc
```

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$

$$
\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
$$

$$
\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc
$$

### Tensors
```latex
T^{\mu \nu} \quad T_{i j k} \quad \mathcal{T}^{ab}_{cd} \quad \sum_{i} T^{i}_{j} e_{i} 
```

$$
T^{\mu \nu} \quad T_{i j k} \quad \mathcal{T}^{ab}_{cd} \quad \sum_{i} T^{i}_{j} e_{i} 
$$

### Linear Algebra
```latex
A \cdot B = \sum_{i,j} A_{ij} B_{ji} \\
\operatorname{tr}(A) = \sum_{i} A_{ii} \\
A^{-1} A = I \\
\lambda v = Av
```

$$
A \cdot B = \sum_{i,j} A_{ij} B_{ji} \\
$$

$$
\operatorname{tr}(A) = \sum_{i} A_{ii} \\
$$

$$
A^{-1} A = I \\
$$

$$
\lambda v = Av
$$

### Eigenvalues and Eigenvectors
```latex
\det(A - \lambda I) = 0 \\
A v = \lambda v
```

$$
\det(A - \lambda I) = 0 \\
$$

$$
A v = \lambda v
$$

### Vector Analysis
```latex
\nabla \cdot \mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z} \\
\nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
F_x & F_y & F_z \end{vmatrix}
```

$$
\nabla \cdot \mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z} \\
$$

$$
\nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
F_x & F_y & F_z \end{vmatrix}
$$

### Complex Numbers
```latex
i^2 = -1, \quad e^{i\pi} + 1 = 0 \\
z = a + ib, \quad \bar{z} = a - ib, \quad |z| = \sqrt{a^2 + b^2} \\
\operatorname{Re}(z) = \frac{z + \bar{z}}{2}, \quad \operatorname{Im}(z) = \frac{z - \bar{z}}{2i}
```

$$
i^2 = -1, \quad e^{i\pi} + 1 = 0 \\
$$

$$
z = a + ib, \quad \bar{z} = a - ib, \quad |z| = \sqrt{a^2 + b^2} \\
$$

$$
\operatorname{Re}(z) = \frac{z + \bar{z}}{2}, \quad \operatorname{Im}(z) = \frac{z - \bar{z}}{2i}
$$

### Fourier and Laplace Transforms
```latex
\mathcal{F}\{f(t)\} = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt \\
\mathcal{L}\{f(t)\} = \int_{0}^{\infty} f(t) e^{-st} dt
```

$$
\mathcal{F}\{f(t)\} = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt \\
$$

$$
\mathcal{L}\{f(t)\} = \int_{0}^{\infty} f(t) e^{-st} dt
$$

### Differential Equations
```latex
y'' + p(x)y' + q(x)y = r(x) \\
\frac{dN}{dt} = -\lambda N \\
N(t) = N_0 e^{-\lambda t}
```

$$
y'' + p(x)y' + q(x)y = r(x) \\
$$

$$
\frac{dN}{dt} = -\lambda N \\
$$

$$
N(t) = N_0 e^{-\lambda t}
$$

For a comprehensive list of LaTeX symbols, see the [Comprehensive LaTeX Symbols List](http://mirror.ctan.org/info/symbols/comprehensive).

# Forward propagation
$\hat y = wx + b$

# Loss Calculation
$L = (y - \hat y)^2$

# Weight and bias update
$\hat w = w - \eta \frac{\partial L}{ \partial w}$ \
$\hat b = b - \eta \frac{\partial L}{\partial b} $

# Weight update

## partial computation
$\frac{\partial L}{ \partial w} = \frac{\partial (y - \hat y)^2}{\partial w}$ \
$ = \frac{\partial (y - wx + b)^2}{\partial w}$ \
$ = 2(y - wx + b)\frac{\partial (y - wx + b)}{\partial w}$ \
$ = 2x(y - wx + b)$ \
$ = 2x(y - \hat y)$

## update
$\hat w = w - 2\eta x (y - \hat y)$
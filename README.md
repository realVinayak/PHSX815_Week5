# PHSX815_Week5
`rejection_sampling.py` contains rejection sampling 
algorithm to sample out of a sinusoidal distribution.<br/>
The sinusoidal function is chosen to be $f(x) = \frac{\pi}{2}\sin{\pi x}$.
The range of x is chosen to be $0 \leq x \leq 1$. It can verified
that the $f(x)$ is normalized in that interval.
<br/>
To run the code, type `python3 rejection_sampling.py`. `N_SAMPLES = 1000000` defined in `rejection_sampling.py`
will be generated through rejection sampling.
<br/>
The output image is stored in `./outputs/sin_hist.png` and the samples
generated are stored in `./outputs/samples.txt`.

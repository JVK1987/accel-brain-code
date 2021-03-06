# -*- coding: utf-8 -*-
from accelbrainbase.samplabledata.noise_sampler import NoiseSampler
import mxnet.ndarray as nd
import mxnet as mx


class UniformNoiseSampler(NoiseSampler):
    '''
    The class to draw fake samples from uniform distributions,
    generating from a `mxnet.ndarray.random`.

    References:
        - Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., ... & Bengio, Y. (2014). Generative adversarial nets. In Advances in neural information processing systems (pp. 2672-2680).

    '''

    def __init__(
        self, 
        low=0.0,
        high=1.0,
        batch_size=40,
        seq_len=0,
        channel=3,
        height=96,
        width=96,
        ctx=mx.gpu()
    ):
        '''
        Init.

        Args:
            low:            `float` of lower boundary of the output interval.
                            All values generated will be greater than or equal to `low`.

            high:           `float` of upper boundary of the output interval.
                            All values generated will be less than or equal to `high`.

            batch_size:     `int` of batch size.
            seq_len:        `int` of the length of series.
                            If this value is `0`, the rank of matrix generated is `4`. 
                            The shape is: (`batch_size`, `channel`, `height`, `width`).
                            If this value is more than `0`, the rank of matrix generated is `5`.
                            The shape is: (`batch_size`, `seq_len`, `channel`, `height`, `width`).

            channel:        `int` of channel.
            height:         `int` of image height.
            width:          `int` of image width.
            ctx:            `mx.gpu` or `mx.cpu`.
        '''
        self.__low = low
        self.__high = high
        self.__batch_size = batch_size
        self.__seq_len = seq_len
        self.__channel = channel
        self.__height = height
        self.__width = width
        self.__ctx = ctx

    def draw(self):
        '''
        Draw samples from distribtions.
        
        Returns:
            `Tuple` of `mx.nd.array`s.
        '''
        if self.__seq_len > 0:
            shape_tuple = (
                self.__batch_size,
                self.__seq_len, 
                self.__channel,
                self.__height,
                self.__width
            )
        else:
            shape_tuple = (
                self.__batch_size,
                self.__channel, 
                self.__height,
                self.__width
            )

        observed_arr = nd.random.uniform(
            low=self.__low, 
            high=self.__high, 
            shape=shape_tuple,
            ctx=self.__ctx
        )

        if self.noise_sampler is not None:
            observed_arr = observed_arr + self.noise_sampler.draw()

        return observed_arr

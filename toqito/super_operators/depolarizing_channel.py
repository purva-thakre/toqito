"""Produces a depolarizng channel"""
import numpy as np
from scipy.sparse import identity
from toqito.states.max_entangled import max_entangled


def depolarizing_channel(dim: int, p: int = 0) -> np.ndarray:
    """
    Produces the depolarizng channel.

    The depolarizng channel is the Choi matrix of the completely depolarizng channel
    that acts on `dim`-by-`dim` matrices.

    Produces the partially depolarizng channel `(1-P)*D + P*ID` where `D` is
    the completely depolarizing channel and `ID` is the identity channel.

    :param dim: The dimensionality on which the channel acts.
    :param p: Default 0.
    """
    # Compute the Choi matrix of the depolarizng channel.

    # Gives a sparse non-normalized state.
    psi = max_entangled(dim, True, False)
    if not isinstance(psi, np.ndarray):
        psi = psi.toarray()

    return (1-p)*identity(dim**2)/dim + p * (psi*psi.conj().T)
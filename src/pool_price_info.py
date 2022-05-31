import os

import web3
from abi.pool_univ3 import pool_abi

alchemy_token = os.getenv("ALCHEMYAPI_TOKEN")


W3 = web3.Web3(
    web3.Web3.HTTPProvider(
        f"https://eth-mainnet.alchemyapi.io/v2/{alchemy_token}",
    ),
)

# cte for price calc
BASE = 1.0001
DECIMAL_DIFF = 10


def get_pool_btc_tick():
    pool = W3.eth.contract(
        address="0xe15e6583425700993bd08F51bF6e7B73cd5da91B", abi=pool_abi
    )

    _, currentTick, _, _, _, _, _ = pool.functions.slot0().call()

    price = (BASE ** currentTick) / 10 ** DECIMAL_DIFF

    return f"{round(1 / price, 6)} WBTC/BADGER"


def main():
    print(get_pool_btc_tick())


if __name__ == "__main__":
    main()

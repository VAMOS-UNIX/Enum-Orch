class Plugin:
    name = "base"
    async def run(self, target: str):
        raise NotImplementedError

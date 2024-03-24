import asyncio
from dotenv import load_dotenv

load_dotenv()
from gpt_python_sandbox.bot import bot, dp


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))

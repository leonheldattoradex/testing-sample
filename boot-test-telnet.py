import unittest
import telnetlib3
import asyncio
import time
import xmlrunner


class TelnetPromptTest(unittest.TestCase):
    TELNET_HOST = "192.168.15.3"
    TELNET_PORT = 9000
    TIMEOUT = 40
    PROMPT = "verdin-imx8mp-06817296 login:"

    async def check_prompt(self):
        reader, writer = await telnetlib3.open_connection(self.TELNET_HOST, self.TELNET_PORT)
        start_time = time.time()
        received_data = ""

        try:
            while time.time() - start_time < self.TIMEOUT:
                chunk = await reader.read(1024)
                if chunk:
                    print(chunk, end="")
                    received_data += chunk

                    if self.PROMPT in received_data:
                        print(f"\nFound expected prompt '{self.PROMPT}'")
                        return True
                else:
                    await asyncio.sleep(0.1)

            self.fail(f"Expected prompt '{self.PROMPT}' not found within {self.TIMEOUT} seconds.")
        finally:
            writer.close()

    def test_wait_for_PROMPT(self):
        asyncio.run(self.check_prompt())


if __name__ == "__main__":
    with open("telnet_test_results.xml", "wb") as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), exit=False)

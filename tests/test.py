import unittest
from click.testing import CliRunner
from crt.cli import main


class TestMain(unittest.TestCase):
    def test_main(self):
        runner = CliRunner()
        result = runner.invoke(main, ["file", "-n", "asd.py"])

        self.assertEqual(result.exit_code, 0)


if __name__ == '__main__':
    unittest.main()

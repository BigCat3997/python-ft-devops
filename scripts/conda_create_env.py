import json
import os
import subprocess
import sys

from entrypoint import show_banner


def create_new_env_if_not_exist(env_name, python_version):
    """Create new conda environment if it was not exist.

    Args:
        env_name: Name of environment.
        python_version: Version of Python.
    """

    search_env_cmd = f"""
        conda env list | grep "^{env_name} "
    """

    search_env_result = subprocess.run(
        search_env_cmd, shell=True, capture_output=True, text=True
    )

    if search_env_result.stderr != "":
        print(search_env_result.stderr)
        print("Exiting the program...")
        sys.exit(0)

    if search_env_result.stdout != "":
        print("The env was exist \n {}".format(search_env_result.stdout))
    else:
        create_new_env_cmd = f"""
            conda create -n {env_name} python={python_version} -y
        """
        create_new_env_result = subprocess.run(
            create_new_env_cmd, shell=True, capture_output=True, text=True
        )
        print(create_new_env_result.stdout)


def execute(env_names_env, python_version_env=None):
    env_names = json.loads(env_names_env)

    for en in env_names:
        create_new_env_if_not_exist(en, python_version_env)


if __name__ == "__main__":
    env_names_env = os.environ.get("ONE_PRESS_ENV_NAMES", '[ "conda1", "conda2" ]')
    python_version_env = os.environ.get("ONE_PRESS_PYTHON_VERSION", "3.10")

    show_banner()
    file_name = sys.argv[0]
    print("The {} file has executed.".format(file_name))
    execute(env_names_env, python_version_env)

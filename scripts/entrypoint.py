import os


def show_banner():
    app_version_env = os.environ.get("ONE_PRESS_APP_VERSION", "v1.0.0")

    print(
        f"""

        ██████╗ ███╗   ██╗███████╗    ██████╗ ██████╗ ███████╗███████╗███████╗
        ██╔═══██╗████╗  ██║██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ██║   ██║██╔██╗ ██║█████╗      ██████╔╝██████╔╝█████╗  ███████╗███████╗
        ██║   ██║██║╚██╗██║██╔══╝      ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║
        ╚██████╔╝██║ ╚████║███████╗    ██║     ██║  ██║███████╗███████║███████║
        ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
                                                                        {app_version_env}

        """
    )

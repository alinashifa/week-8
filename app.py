{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/alinashifa/week-8/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "T_VFbgHPiFJG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6bf92299-1450-4870-d1bb-2f59a049225e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K     |████████████████████████████████| 10.3 MB 5.2 MB/s \n",
            "\u001b[K     |████████████████████████████████| 164 kB 55.4 MB/s \n",
            "\u001b[K     |████████████████████████████████| 237 kB 53.2 MB/s \n",
            "\u001b[K     |████████████████████████████████| 4.7 MB 40.3 MB/s \n",
            "\u001b[K     |████████████████████████████████| 182 kB 77.5 MB/s \n",
            "\u001b[K     |████████████████████████████████| 78 kB 6.6 MB/s \n",
            "\u001b[K     |████████████████████████████████| 62 kB 1.3 MB/s \n",
            "\u001b[K     |████████████████████████████████| 51 kB 6.8 MB/s \n",
            "\u001b[?25h  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n"
          ]
        }
      ],
      "source": [
        "!pip install -q streamlit"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c_1YkpDWqx6n",
        "outputId": "18047fa9-c5f9-4fa2-b5ea-8f34c7fcae3c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/gdrive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/gdrive')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qer8mEjCiSNS",
        "outputId": "0099748d-495d-44f1-e62e-9d32c56abc7b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2022-11-30 13:27:32--  https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip\n",
            "Resolving bin.equinox.io (bin.equinox.io)... 18.205.222.128, 52.202.168.65, 54.161.241.46, ...\n",
            "Connecting to bin.equinox.io (bin.equinox.io)|18.205.222.128|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 13832437 (13M) [application/octet-stream]\n",
            "Saving to: ‘ngrok-stable-linux-amd64.zip’\n",
            "\n",
            "ngrok-stable-linux- 100%[===================>]  13.19M  58.6MB/s    in 0.2s    \n",
            "\n",
            "2022-11-30 13:27:33 (58.6 MB/s) - ‘ngrok-stable-linux-amd64.zip’ saved [13832437/13832437]\n",
            "\n"
          ]
        }
      ],
      "source": [
        "!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WPUvoENLiK7u",
        "outputId": "fc600f07-2e0f-4079-e9c0-9e9cc5633ce1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archive:  ngrok-stable-linux-amd64.zip\n",
            "  inflating: ngrok                   \n"
          ]
        }
      ],
      "source": [
        "!unzip ngrok-stable-linux-amd64.zip"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bh5Vc0MCQ2yw",
        "outputId": "6aaa0338-7035-4082-82d4-90210fa1a209"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Authtoken saved to configuration file: /root/.ngrok2/ngrok.yml\n"
          ]
        }
      ],
      "source": [
        "! /content/ngrok authtoken 22cld42QqSya4Ars9jYrv7DCwm6_3Sdy6vAsYp5XR2NLdpRg5"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "2mzhUMngxa8z"
      },
      "outputs": [],
      "source": [
        "get_ipython().system_raw('./ngrok http 8501 &')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DOxrBiwbxfqT",
        "outputId": "4cc8de46-1674-4a37-d47a-da529a13d1db"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Traceback (most recent call last):\n",
            "  File \"<string>\", line 1, in <module>\n",
            "  File \"/usr/lib/python3.7/json/__init__.py\", line 296, in load\n",
            "    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)\n",
            "  File \"/usr/lib/python3.7/json/__init__.py\", line 348, in loads\n",
            "    return _default_decoder.decode(s)\n",
            "  File \"/usr/lib/python3.7/json/decoder.py\", line 337, in decode\n",
            "    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n",
            "  File \"/usr/lib/python3.7/json/decoder.py\", line 355, in raw_decode\n",
            "    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\n",
            "json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)\n"
          ]
        }
      ],
      "source": [
        "!curl -s http://localhost:4040/api/tunnels | python3 -c \\\n",
        "    'import sys, json; print(\"Execute the next cell and the go to the following URL: \" +json.load(sys.stdin)[\"tunnels\"][0][\"public_url\"])'"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ccpi-aiSxk_U",
        "outputId": "4bc16eed-8b2a-408e-9b0e-3268b6de4702"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.2:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.185.3.113:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n"
          ]
        }
      ],
      "source": [
        "! streamlit run /content/gdrive/MyDrive/app.py"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_MPWDunzxpRF"
      },
      "outputs": [],
      "source": [
        "!pip3 freeze > requirements.txt"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "hrZUKAixc2tH"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
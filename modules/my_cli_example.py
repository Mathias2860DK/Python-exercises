{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import argparse\n",
    "def printCsv():\n",
    "        parser = argparse.ArgumentParser(\n",
    "        description='A program that store csv rows in a list')\n",
    "        parser.add_argument('file_path', help='The path to the file')\n",
    "\n",
    "        args = parser.parse_args()\n",
    "        print('file_path:', args.file_path)\n",
    "\n",
    "        my_list = []\n",
    "        with open(args.file_path) as f_obj:\n",
    "            content = f_obj.readlines()\n",
    "\n",
    "        for line in content[:20]:\n",
    "            my_list.append(line.strip().split(','))\n",
    "        print(my_list)\n",
    "printCsv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

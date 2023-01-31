# Content of Project

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detailed information about modules](#more-detailed-information-about-modules)
* [Contact](#Contact)

## General info
<details>
<summary>Click here to see general information about <b>Cipher</b>!</summary>
<b>Cipher project</b>. This project was made as a part of Devs-Mentoring Python Developer course. The program allows the user to encrypt or decrypt text using the Rot13 or Rot47 cipher. The program can be extended with further ciphers. The encrypted/decrypted text can be saved as a .json file.
</details>

## Technologies
<ul>
Project is created with:
 <li>Python 3.10</li>
 <li>Pytest 7.2.1</li>
 <li>Pre-commit 2.3.0</li>
</ul>

## Setup

To start this project run main.py

## More detailed information about modules
This program was build based on OOP principles, inheritance, multicomposition and Abstract Factory creational design pattern. The project is divided into two folders: functionality and tests. Functionality folder contains modules responsible for the functioning of the program. Tests folder containts tests modules.

<br>The modules contained in the folder functionality are:<br>

<b>buffer.py</b> - creates buffer where encrypt or decrypt text can be storage<br>
<b>filehandler.py</b> - allows the user to save text in a .json file, upload or create a file<br>
<b>main.py</b> - starts programm <br>
<b>manager.py</b> - multicomposition of methods and objects<br>
<b>menu.py</b> - messages appearing in the program menu<br>
<b>rot.py</b> - encoding and decoding text using Rot13 and Rot47, creating a RotFactory <br>

## Contact
Wojciech Zaczek - wojciech.zaczek84@gmail.com

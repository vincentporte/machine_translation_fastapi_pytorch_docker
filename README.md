<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU General Public License v3.0][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">char level seq2seq machine translation</h3>

  <p align="center">
    character level machine translation, using fastapi, pytorch sequence 2 sequence model and docker
    <br />
    <a href="https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker/issues">Report Bug</a>
    ·
    <a href="https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

You can use this project to easily setup a machine translation api for authenticated user. You can add your own translation in database, train your models using these translation and deploy it like a charm.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* [FastAPI users](https://fastapi-users.github.io/)
* [Pytorch](https://pytorch.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Nginx](https://www.nginx.com/)
* [Docker](https://www.docker.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites (based on Ubuntu 20.04 LTS)

* Update existing packages, and install a few prerequisite packages which let apt use packages over HTTPS
  ```sh
  sudo apt update && sudo apt upgrade -y
  sudo apt install -y apt-transport-https ca-certificates curl software-properties-common gnupg-agent
  ```
* Add docker signin keys
  ```sh
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  ```
* Verify signature
  ```sh
  sudo apt-key fingerprint 0EBFCD88
  ```
  output must look like
  ```sh
  pub   rsa4096 2017-02-22 [SCEA]
        9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
  uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
  sub   rsa4096 2017-02-22 [S]
  ```
* Add docker repository
  ```sh
  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  sudo apt-get update  ```
* Install docker
  ```sh
  sudo apt-get install docker-ce docker-ce-cli containerd.io -y
  ```
* Add user to docker group
  ```sh
  sudo usermod -a -G docker $USER
  ```
  then logout
* Install docker-compose v2.2.2 (latest at 2021-12-29)
  ```sh
  sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  ```

### Installation

* Clone the repo
  ```sh
  git clone https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker.git
  ```
* Build the docker image
  ```sh
  docker-compose build backend
  ```
* Setup keys and credentials in `.env`
  ```python
  POSTGRES_USER=db_user
  POSTGRES_PASSWORD=db_pass
  POSTGRES_DB=db_name
  SECRET_KEY=secret_key_for_users_management
  DATABASE_URL=postgres://db_user:db_pass@db:5432/db_name
  ```
* Run your containers
  ```sh
  docker-compose up -d;docker-compose logs -f
  ```
* Init you database
  ```sh
  docker-compose exec backend aerich init-db
  ```
* Run tests
  ```sh
  docker-compose exec backend pytest

### Setup superuser (after you registered it through API endpoint)
* Access DB cmd line
  ```sh
  docker exec -it mt_db psql -U db_user -h 127.0.0.1 -W db_name
  ```
* Grant superuser rigths
  ```sh
  UPDATE usermodel SET is_superuser = 't', is_verified = 't' WHERE email = 'superuser@domain.com';
  ```

### Upgrade Database Model
* Generate migration file
  ```sh
  docker-compose exec backend aerich migrate
  ```
* Apply upgrade to DB
  ```sh
  docker-compose exec backend aerich upgrade
  ```

### Deployement

* Replace /config/nginx/nginx.conf with nginx.conf.live
* Update server_name refs
  ```sh
  server_name subdomain.domain.com;
  ```
* Add CAA record in your DNS
  ```sh
  sudomain.domain.com. CAA 0 issue letsencrypt.org
  ```
* Update refs in letsencrypt.sh
  ```sh
  domains=(subdomain.domain.com)
  email="contact@domain.com"
  ```
* Run letsencrypt.sh script to setup certificates
  ```sh
  exec sudo ./init-letsencrypt.sh
  ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* Register new user
  ```sh
  http://localhost/auth/register
  ```
* Log in
  ```sh
  http://localhost/auth/login
  ```


_For more examples, please refer to the [Documentation](http://localhost/docs)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] Train translation model with users dataset
    - [] add translation pairs in DB
    - [] extract dataset and train pytorch model
- [] User Verification by email
    - [] setup mailgun API Key
- [] Named entity recognition to extract part of text to translate
    - [] setup spay

See the [open issues](https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Vincent PORTE - contact@neuralia.co

Project Link: [https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker](https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [How To Install and Use Docker Compose on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)
* [Certificate Authority Authorization (CAA)](https://letsencrypt.org/docs/caa/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/vincentporte/machine_translation_fastapi_pytorch_docker.svg?style=for-the-badge
[contributors-url]: https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/vincentporte/machine_translation_fastapi_pytorch_docker.svg?style=for-the-badge
[forks-url]: https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker/network/members
[stars-shield]: https://img.shields.io/github/stars/vincentporte/machine_translation_fastapi_pytorch_docker.svg?style=for-the-badge
[stars-url]: https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker/stargazers
[issues-shield]: https://img.shields.io/github/issues/vincentporte/machine_translation_fastapi_pytorch_docker.svg?style=for-the-badge
[issues-url]: https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker/issues
[license-shield]: https://img.shields.io/github/license/vincentporte/machine_translation_fastapi_pytorch_docker.svg?style=for-the-badge
[license-url]: https://github.com/vincentporte/machine_translation_fastapi_pytorch_docker/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/vincentporte
[product-screenshot]: images/screenshot.png
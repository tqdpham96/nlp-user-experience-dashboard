<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
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
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tqdpham96/nlp-user-experience-dashboard">
    <img src="images/logo.jpeg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Customer Experience Dashboard</h3>

  <p align="center">
    The Customer Experience Dashboard is my personal fun project designed to provide comprehensive insights into customer interactions and satisfaction levels of pubs in Wilmslow, UK. This dynamic dashboard acts as a centralized hub, aggregating data from various touchpoints such as customer support interactions, product reviews, and social media sentiments. The primary goal is to empower businesses to holistically understand and enhance their customer experience.
    <br />
    <a href="https://github.com/tqdpham96/nlp-user-experience-dashboard">View Demo</a>
    ·
    <a href="https://github.com/tqdpham96/nlp-user-experience-dashboard/issues">Report Bug</a>
    ·
    <a href="https://github.com/tqdpham96/nlp-user-experience-dashboard/issues">Request Feature</a>
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

[![Product Name Screen Shot][product-screenshot]](https://smark-pub-review.streamlit.app/)

Hello everyone! I wanted to share a little project I worked on over the Christmas break while in Europe. With everything settled down, I was looking for something enjoyable to lift my spirits. While randomly surfing the internet, I stumbled upon some fantastic resources and libraries related to Generative AI and NLP. Intrigued, I decided to test the capabilities of these libraries to gauge how close we are to state-of-the-art solutions.

As a result, I chose to create a customer service dashboard for all the pubs in my friend's hometown, Wilmslow, UK :D. The data for this fun project is crawled from Google Map reviews. Keep in mind that this is designed as a light-hearted project, perfect for students new to software engineering and AI which covers lots of realize problem in the field of NLP/AI. There's room for implementing various technologies like APIs and data crawling to enhance the project further, but unfortunately, I currently lack the time, and it's a bit too much on the serious side for my definition of 'fun' :D. 

Here are some details about the project:

* The project involves data crawling from Google Map Reviews, utilizing tools like Python BeautifulSoup, the Google extension Scraper Crawler V3, or third-party solutions such as APIFY.
* For the user interface, Streamlit is employed, seamlessly integrated with ECharts and Plotly for robust data visualization.
* In the realm of NLP/AI tasks, the project encompasses Sentiment Analysis, Emotional Analysis, Keywords Extraction, Chat-GPT, and more.
* Algorithmic tasks include Co-occurrence Matrix and Matrix Multiplication, contributing to the project's analytical depth.
* The server deployment is achieved using Streamlit community cloud or the Heroku cloud platform, ensuring accessibility and efficiency.

Here are some improvement can be made to the project:

* Ensure efficient data loading by integrating a database into the infrastructure, with a preference for NoSQL for enhanced performance.
* Elevate the project with real-time data instead of static information by implementing 1-2 cron jobs to periodically scan the pubs.
* Provide users with the option to automatically crawl Google review data, enhancing the project's flexibility and user experience.
* Implement reporting functionalities to offer users insights and analysis based on the gathered data.

Enjoy!!!
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* Python
* Streamlit
* Heroku
* OpenAI
<!-- * [![Python][https://www.python.org/]][Python-url]
* [![Streamlit][https://streamlit.io/]][Streamlit-url]
* [![Heroku][heroku.com]][Heroku-url]
* [![OpenAI][openai.com]][OpenAI-url] -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Lets get started!!!

### Prerequisites

Install the requirement libraries.
* python
  ```sh
  python-3.10.9
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/tqdpham96/nlp-user-experience-dashboard.git
   ```

2. Install pip packages
   ```sh
   pip install -r requirements. txt
   ```

3. Create Heroku account/Streamlit account

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* Summary Google Review Rating
* Sentiment analysis these reviewes to Positive + Negative + Neutral
* Sentiment Monthly Trend
* Sentiment Score 
* Sentiment Score Monthly Trend
* Entity by Sentiment
* Emotional Words (Positive and Negative)
* Word Cloud (Entity and Emotion)
* Customer's Voice analysis
* Aspect Co-occurence
* Emotion Aspect Co-occurence
* Favourite/Hated Customers
* Comparison between two pubs
* AI/NLP Tool (Chatbot + Sentiment)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add NoSQL Database
- [ ] Add Cronjob for data crawling
- [ ] Add Additional Feature if needed
- [ ] Multi-language Support
    - [ ] French
    - [ ] Germany

See the [open issues](https://github.com/tqdpham96/nlp-user-experience-dashboard/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Dr. T.Q.D. Pham -  pqducthinhbka@gmail.com

Project Link: [https://github.com/tqdpham96/nlp-user-experience-dashboard](https://github.com/tqdpham96/nlp-user-experience-dashboard)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [NLP Book for beginners](https://shop.elsevier.com/books/the-natural-language-for-artificial-intelligence/motta-monte-serrat/978-0-12-824118-9?country=BE&format=print&utm_source=google_ads&utm_medium=paid_search&utm_campaign=belgiumpmax&gad_source=1&gclid=CjwKCAiAhJWsBhAaEiwAmrNyq6LVvCzV8ioiR2rLCUvytJb65puQO7zUvwN_OqIdFdgBqloS2V-gBxoCHMkQAvD_BwE&gclsrc=aw.ds)
* [Deep Learning](https://www.amazon.com.be/-/nl/Seth-Weidman/dp/1492041416/ref=asc_df_1492041416/?tag=begogshpadd0d-21&linkCode=df0&hvadid=633075841889&hvpos=&hvnetw=g&hvrand=2122455334606967236&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001394&hvtargid=pla-716776504046&psc=1&mcid=69a6db17338c3897862a3c0cb4dfd658)
* [MLOps](https://www.bol.com/be/nl/p/introducing-mlops-how-to-scale-machine-learning-in-the-enterprise/9300000008109732/?Referrer=ADVNLGOO002008N-S--9300000008109732&gad_source=1&gclid=CjwKCAiAhJWsBhAaEiwAmrNyq-dSoath1cEtg2Y9zuX8F3XPWGZGunuYnY6COPoEKb6j0Tx4Yh5TlRoCT50QAvD_BwE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/preview.png
[Python]: https://www.python.org/static/img/python-logo@2x.png
[Python-url]: https://www.python.org/
[Streamlit]: https://streamlit.io/images/brand/streamlit-mark-color.svg
[Streamlit-url]: https://streamlit.io/
[Heroku]: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRitRYJmyZ3IrHw5Pryim_gGQdOZITn90g-Wvd9F87RehP9Tw3An_mFKE9OqtA1kJXQ_A&usqp=CAU
[Heroku-url]: https://heroku.com/
[OpenAI]: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCX5oU1OHZxG4Hws6jr2brvyQuwDZGJ9ixaAKojBcAag&s
[OpenAI-url]: https://openai.com/
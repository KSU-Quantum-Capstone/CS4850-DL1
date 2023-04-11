---
layout: page
title: Contributing to the Project Website
permalink: /docs/contributing-website/
parent: Docs
nav_order: 4
---

# Getting Started with the Website

Note: these steps are for MacOS/Linux/Unix but you will most likely run into problems installing Jekyll on Windows. See more information here: [Jekyll on Windows](https://jekyllrb.com/docs/installation/windows/)

To contribute to the project website, you will need to follow the steps outlined below.

1. Create a new anaconda environment used specifically for the gh-pages branch `conda create --name gh-pages`
2. Activate the new environment with `conda activate gh-pages`
3. Install the necessary anaconda packages `conda install -c conda-forge c-compiler compilers cxx-compiler ruby`
4. Install jekyll and bundler `gem install jekyll bundler`
5. Clone the repository with `git clone https://github.com/KSU-Quantum-Capstone/CS4850-DL1.git`.
6. Navigate into the git repository on your local computer with the `cd` command. Once you are in `.../CS4850-DL1/`,
7. Switch to the gh-pages branch `git checkout gh-pages`
8. Install the bundle's prerequisites `bundle install`
9. Start the jekyll server `bundle exec jekyll serve`
10. Make any necessary changes in the various markdown files. Everytime you save a file, the local jekyll server will reload your changes unless you are editing the \_config.yml file.
11. Stage your changes to the local git repo with the command `git add .`
12. Commit your changes by using the command `git commit -m "Enter summary of the changes you made here"`
13. Push your changes to the remote GitHub repo. `git push origin`
14. End the server with `ctrl+c`
15. Close your conda environment with `conda deactivate`

# My Two Cents 

When installing and Learning about Atlassian Forge, I went through some curveballs. 

* Understanding that Forge is not a language. It is an Atlassian tool that is meant to add functionality to Atlassian Products, for example, Jira.
* Installing npm packages globally resulted in write access errors
* My Linux Ubuntu Node.js version could not work with the Forge CLI. The Erbium stable version 12.22.11 ended up working.
* When installing and setting up Docker, do give non-root users access. Otherwise, Forge will not work as expected, for example, I could not get tunnelling to work, and I had to keep running docker commands using sudo.
* Your user credentials on Docker Hub need to be the same as those on the Docker CLI.
* You run 'forge deploy' before 'forge install'


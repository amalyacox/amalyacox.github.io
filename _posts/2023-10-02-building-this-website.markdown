This website was initially difficult for me to build. Here is the (ongoing) story: 

1. I am introduced to github pages and Jekyll. It seems like a straightforward way to build this website. I quickly realize that in order to install Jekyll, I need Ruby, and in order to get Ruby working, I need WSL (Windows Subsystem for Linux).

2. I successfully install WSL and attempt to follow the Ruby and Jekyll installation. No dice. I give up on the website for about a year. 

3. Fall 2023. I return to attempting to build this website. This can't be so hard, right? This time I decide to actually read what the errors were giving me. 

4. Long story short, versions of certain Ruby gems were not matching my Gemfile or Gemfile.Lock or the github-pages requirements. I needed to update these things to have all the adequate dependencies.

5. Also, I think because of WSL there were a lot of commands I had to run as sudo. Initially ran into writing permission errors as well.

6. In addition to reading and addressing the errors. I asked Chat-GPT for help. Did Chat-GPT help me? Probably not actually. It mostly just told me what stack overflow was telling me. However it was helpful to just have a place to take my issues to. It gave me step by step (attempts) at answers, which was nice. 

7. Here we are with a semi-working website. Still building and trying to add to it. 

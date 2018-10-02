async function githubRepos() {
  let github_repos_response = await fetch('https://api.github.com/users/julian-garcia/repos');
  let github_repos = await github_repos_response.json();
  let github_div = document.querySelector('.github');

  github_repos.forEach(function(repo) {
    let repo_link = document.createElement('a');
    repo_link.textContent = repo.name;
    repo_link.href = repo.html_url;
    repo_link.setAttribute('target', '_blank');
    repo_link.className = 'github-button button is-light is-rounded is-medium';
    github_div.append(repo_link);
  });
}

githubRepos();

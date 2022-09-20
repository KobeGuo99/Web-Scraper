from bs4 import BeautifulSoup
import requests


def find_jobs(url, unfamiliar):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' or 'today' or '1 day' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar.lower() == 'nothing':
                unfamiliar = '¤¤¤¤¤¤sdsdsfedgrghbsfc'
            if unfamiliar not in skills.lower():
                with open(f'posts/job_{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More info: {more_info}')
                print(f'File saved: {index}')


if __name__ == '__main__':
    scrape_continue = True
    while scrape_continue:
        print('Enter the website url from timesjobs.com you want to scrape')
        website_url = input('> ')

        print('Put some skill that you are not familiar with (Put nothing if there\'s no skill unfamiliar)')
        unfamiliar_skill = input('> ').lower()
        print(f'Filtering out {unfamiliar_skill}')

        find_jobs(website_url, unfamiliar_skill)

        question_continue = input('Do you want to scrape again? Make sure to have the posts folder empty if you do ('
                                  'Y/N) ')
        if question_continue.lower() != 'y':
            scrape_continue = False

        

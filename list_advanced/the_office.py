happiness_scores = list(map(int, input().split()))
improvement_factor = int(input())

total_count = len(happiness_scores)

improved_happiness = [score * improvement_factor for score in happiness_scores]

average_happiness = sum(improved_happiness) / total_count

happy_count = len([num for num in improved_happiness if num >= average_happiness])

if happy_count >= total_count / 2:
    print(f'Score: {happy_count}/{total_count}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{total_count}. Employees are not happy!')
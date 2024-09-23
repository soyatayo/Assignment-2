
# Load the dataset
df = pd.read_csv(r"C:\Users\sharo\Documents\datasets\imdb-movies-dataset.csv")

# Calculate mean, median, and mode for 'rating'
mean_rating = df['rating'].mean()
median_rating = df['rating'].median()
mode_rating = stats.mode(df['rating'])[0][0]

# Calculate mean, median, and mode for 'votes'
mean_votes = df['votes'].mean()
median_votes = df['votes'].median()
mode_votes = stats.mode(df['votes'])[0][0]

# Print the results
print(f"Rating - Mean: {mean_rating}, Median: {median_rating}, Mode: {mode_rating}")
print(f"Votes - Mean: {mean_votes}, Median: {median_votes}, Mode: {mode_votes}")
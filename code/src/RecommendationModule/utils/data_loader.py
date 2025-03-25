import pandas as pd

def load_data():
    # Load Customer Data
    customer_transactions = pd.read_excel("c:/Hackathon2025/aidhp-recom-mind/code/src/RecommendationModule/Data/CustomerData.xlsx", sheet_name="Transaction history")
    individual_profiles = pd.read_excel("c:/Hackathon2025/aidhp-recom-mind/code/src/RecommendationModule/Data/CustomerData.xlsx", sheet_name="Customer Profile (Individual)")
    org_profiles = pd.read_excel("c:/Hackathon2025/aidhp-recom-mind/code/src/RecommendationModule/Data/CustomerData.xlsx", sheet_name="Customer Profile (Organisation)")
    social_media = pd.read_excel("c:/Hackathon2025/aidhp-recom-mind/code/src/RecommendationModule/Data/CustomerData.xlsx", sheet_name="Social Media Sentiment")

    # Load Local Providers Data
    providers = pd.read_excel("c:/Hackathon2025/aidhp-recom-mind/code/src/RecommendationModule/Data/Expanded_LocalProviders.xlsx", sheet_name="Sheet1")

    return customer_transactions, individual_profiles, org_profiles, social_media, providers


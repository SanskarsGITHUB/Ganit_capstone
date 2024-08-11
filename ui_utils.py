import streamlit as st
import random
from datetime import datetime

# Sample news content with associated image URLs
news_content = [
    {
        "text": "As India celebrates Vinesh Phogat's historic performance at the 2024 Paris Olympics, RTI findings reveal that the investigation into allegations of sexual misconduct against Brij Bhushan Singh remains shrouded in secrecy. In response to an RTI seeking information about the Mary Kom-led oversight committee probing the case, the Sports Ministry claimed, 'this information is not available.'",
        "image": "https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/10_sat/img_1723277404176_181.jpg?"
    },
    {
        "text": "Prime Minister Narendra Modi on Saturday conducted an aerial survey of landslide-affected areas of Kerala's Wayanad. The PM, who also physically visited the affected areas, was accompanied by Kerala Governor Arif Mohammed Khan, Chief Minister Pinarayi Vijayan and Union Minister of State Suresh Gopi. Notably, over 300 people lost their lives after multiple landslides hit Wayanad on July 30.",
        "image": "https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/10_sat/img_1723275648230_273.jpg?"
    },
    {
        "text": "The Dakshina Kannada district police are stepping up their fight against the rising tide of cybercrimes. SP Yathish N expressed concern over the increasing number of educated individuals and professionals falling victim to these crimes. To tackle this, the police have launched enhanced awareness campaigns through social media, sharing short videos on cybercrime prevention.",
        "image": "https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/10_sat/img_1723275847405_761.jpg?"
    },
    {
        "text": "The BSE Sensex dropped 582 points, closing at 78,886, while the NSE Nifty50 fell by 180 points to 24,117. Market volatility continues as global cues weigh heavily. The rupee fell to a record low of 83.96 against the dollar, causing concern among market segments. Meanwhile, India's forex reserves reached $675 billion. Consumer product sales slowed sharply due to macroeconomic headwinds.",
        "image": "https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/9_fri/img_1723182786969_217.jpg?"
    },
    {
        "text": "Shares of Ola Electric listed on BSE on Friday with no premium. Ola Electric had offered shares in its ₹6,154-crore IPO, which was open between August 2 and August 6, at a price band of ₹72-76, with shares listing on Friday at ₹75.99. The shares, however, rose nearly 17.50% in early trade to hit a high of ₹89.25.",
        "image": "https://nis-gs.pix.in/inshorts/images/v1/variants/webp/m/2024/08_aug/10_sat/img_1723268918648_743.webp?"
    },
]

def show_home_page():
    st.markdown("<h1 style='text-align: center; color: #ff6347;'>WELCOME TO GANIT NEWSPAPER</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>Today's Date: {datetime.now().strftime('%B %d, %Y')}</h3>", unsafe_allow_html=True)
    
    # Red strip with app download message
    st.markdown(
        """
        <div style="background-color: #FF6347; color: white; padding: 10px; text-align: center; margin-bottom: 20px;">
            For the best experience, download the app
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Create three columns
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        # Select 5 random news items
        random_news = random.sample(news_content, 5)
        
        for i, news in enumerate(random_news[:2], start=1):  # First 2 news items
            st.markdown(
                f"""
                <div style="border: 2px solid #0066cc; border-radius: 10px; padding: 10px; margin-bottom: 20px;">
                    <h4>News {i}</h4>
                    <img src="{news['image']}" style="width: 100%; border-radius: 10px;"/>
                    <p style="font-size: 12px;">{news['text']}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )

    with col2:
        st.selectbox("Choose an item:", ["Item 1", "Item 2", "Item 3", "Item 4"])
        # Display the 4th news item in the center column
        st.markdown(
            f"""
            <div style="border: 2px solid #009933; border-radius: 10px; padding: 10px; margin-bottom: 20px;">
                <h4>News 4</h4>
                <img src="{news_content[3]['image']}" style="width: 100%; border-radius: 10px;"/>
                <p style="font-size: 12px;">{news_content[3]['text']}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

    with col3:
        for i, news in enumerate(random_news[2:4], start=3):  # Remaining 2 news items
            st.markdown(
                f"""
                <div style="border: 2px solid #ff6600; border-radius: 10px; padding: 10px; margin-bottom: 20px;">
                    <h4>News {i}</h4>
                    <img src="{news['image']}" style="width: 100%; border-radius: 10px;"/>
                    <p style="font-size: 12px;">{news['text']}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )

    if st.button("Back to Home"):
        st.session_state.page = 'home'

# Initialize session state if it does not exist
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Render the appropriate page based on session state
if st.session_state.page == 'home':
    show_home_page()
elif st.session_state.page == 'next_page':
    show_next_page()

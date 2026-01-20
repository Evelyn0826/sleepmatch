import streamlit as st

import streamlit as st
import streamlit.components.v1 as components

GA_MEASUREMENT_ID = "G-VMNM6JJ2M4"

def inject_ga():
    components.html(
        f"""
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{GA_MEASUREMENT_ID}', {{ 'anonymize_ip': true }});
        </script>
        """,
        height=0,
    )

inject_ga()


def base_sleep_by_age(age):
    """Return base sleep hours based on age."""
    if age <= 25:
        return 8.0
    elif age <= 64:
        return 7.5
    else:
        return 7.0

def adjust_for_activity(current_sleep, activity):
    """Adjust sleep based on activity level and return (new_sleep, reason)."""
    if activity == "high":
        return current_sleep + 0.5, "High activity adds 0.5h."
    elif activity == "medium":
        return current_sleep + 0.25, "Medium activity adds 0.25h."
    else:
        return current_sleep, "Low activity adds 0h."

def adjust_for_caffeine(current_sleep, cups):
    """Adjust sleep based on caffeine cups and return (new_sleep, reason)."""
    if cups >= 4:
        return current_sleep + 0.75, "High caffeine (4+ cups) adds 0.75h."
    elif cups >= 2:
        return current_sleep + 0.25, "Moderate caffeine (2-3 cups) adds 0.25h."
    else:
        return current_sleep, "Low caffeine (0-1 cup) adds 0h."

def get_sleep_recommendation(age, activity, cups):
    base = base_sleep_by_age(age)
    after_activity, activity_reason = adjust_for_activity(base, activity)
    final_sleep, caffeine_reason = adjust_for_caffeine(after_activity, cups)

    reason = (
        f"Based on your age ({age}), your base sleep need is {base} hours. "
        f"{activity_reason} {caffeine_reason}")
    return final_sleep, reason

st.set_page_config(page_title="SleepMatch", page_icon="😴")

st.title("😴 SleepMatch")
st.write("Get a sleep recommendation based on age, activity level, and caffeine intake.")

age = st.number_input("Age", min_value=1, max_value=120, value=20, step=1)
activity = st.selectbox("Activity level", ["low", "medium", "high"])
cups = st.number_input("Caffeine cups per day", min_value=0, max_value=10, value=0, step=1)

if st.button("Calculate"):
    target, reason = get_sleep_recommendation(age, activity, cups)
    st.subheader(f"Recommended sleep hours: {target:.2f}")
    st.info(reason)

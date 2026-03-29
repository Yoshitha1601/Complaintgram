import streamlit as st
import json
import os
from datetime import datetime
import random

# ── Config ────────────────────────────────────────────
st.set_page_config(
    page_title="ComplaintGram",
    page_icon="📢",
    layout="wide"
)

DB_FILE = "complaints.json"

# ── Database Functions ────────────────────────────────
def load_complaints():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_complaints(complaints):
    with open(DB_FILE, "w") as f:
        json.dump(complaints, f, indent=2)

def initialize_db():
    if not os.path.exists(DB_FILE):
        seed_data = [
            {
                "id": 1,
                "user": "Ravi_Kondapur",
                "avatar": "🧑",
                "area": "Kondapur",
                "city": "Hyderabad",
                "category": "Road / Pothole / Footpath",
                "complaint": "Massive pothole on Kondapur main road near IKEA signal. 3 bikes fell this week alone. Been here 5 months with zero action from GHMC.",
                "proof": "5 photos + video of bike falling",
                "duration": "2-3 months",
                "severity_score": 9,
                "severity_label": "Critical",
                "authority": "GHMC Zone 13 — Serilingampally",
                "categories": ["Road Safety", "GHMC", "Pothole"],
                "hashtags": "#HyderabadPotholes #GHMC #KondapurRoads #FixOurRoads",
                "upvotes": 247,
                "timestamp": "2026-03-28 09:15",
                "formal_letter": "To,\nThe Zonal Commissioner,\nGHMC Zone 13...",
                "status": "Unresolved"
            },
            {
                "id": 2,
                "user": "Priya_Mehdipatnam",
                "avatar": "👩",
                "area": "Mehdipatnam",
                "city": "Hyderabad",
                "category": "Water Supply / Pipeline",
                "complaint": "No water supply for 6 days in Mehdipatnam colony. HMWSSB tankers not coming. 200+ families affected. Children and elderly suffering in summer heat.",
                "proof": "Photos of empty overhead tank + WhatsApp complaints from 50 residents",
                "duration": "6+ months",
                "severity_score": 9,
                "severity_label": "Critical",
                "authority": "HMWSSB — South Zone",
                "categories": ["Water Crisis", "HMWSSB", "Summer Emergency"],
                "hashtags": "#HyderabadWaterCrisis #HMWSSB #MehdipatnamWater #WaterRight",
                "upvotes": 189,
                "timestamp": "2026-03-28 11:30",
                "formal_letter": "To,\nThe General Manager,\nHMWSSB South Zone...",
                "status": "Unresolved"
            },
            {
                "id": 3,
                "user": "Suresh_Ameerpet",
                "avatar": "👨",
                "area": "Ameerpet",
                "city": "Hyderabad",
                "category": "Garbage / Sanitation",
                "complaint": "Garbage dump overflowing at Ameerpet X roads for 2 weeks. GHMC vehicles not coming. Stench unbearable. Disease risk for nearby schools and hospitals.",
                "proof": "10 photos of garbage mountain + school proximity map",
                "duration": "1 month",
                "severity_score": 8,
                "severity_label": "Critical",
                "authority": "GHMC Sanitation Wing — West Zone",
                "categories": ["Sanitation", "Public Health", "GHMC"],
                "hashtags": "#HyderabadGarbage #GHMC #AmeerpetSanitation #PublicHealth",
                "upvotes": 156,
                "timestamp": "2026-03-27 14:20",
                "formal_letter": "To,\nThe Deputy Commissioner,\nGHMC West Zone...",
                "status": "Unresolved"
            },
            {
                "id": 4,
                "user": "Lakshmi_Miyapur",
                "avatar": "👩",
                "area": "Miyapur",
                "city": "Hyderabad",
                "category": "Electricity / Street Light",
                "complaint": "15 street lights not working on Miyapur to Chandanagar road for 3 weeks. Women feel unsafe walking at night. Two chain snatching incidents happened in dark stretch.",
                "proof": "Night photos showing darkness + police complaint copy",
                "duration": "1 month",
                "severity_score": 8,
                "severity_label": "Critical",
                "authority": "TSSPDCL — Miyapur Division",
                "categories": ["Women Safety", "Street Lights", "TSSPDCL"],
                "hashtags": "#MiyapurDark #WomenSafety #TSSPDCL #StreetLights",
                "upvotes": 134,
                "timestamp": "2026-03-27 18:45",
                "formal_letter": "To,\nThe Divisional Engineer,\nTSSPDCL Miyapur...",
                "status": "Unresolved"
            },
            {
                "id": 5,
                "user": "Ahmed_Tolichowki",
                "avatar": "🧑",
                "area": "Tolichowki",
                "city": "Hyderabad",
                "category": "Drainage / Flooding",
                "complaint": "Drain blocked at Tolichowki junction causing road flooding every time it rains. Shops and homes flooded twice this month. Kids falling sick from contaminated water.",
                "proof": "Video of flooding + medical bills of affected children",
                "duration": "2-3 months",
                "severity_score": 7,
                "severity_label": "High",
                "authority": "GHMC Drainage Wing",
                "categories": ["Flooding", "Drainage", "Public Health"],
                "hashtags": "#TolichowkiFlooding #GHMC #DrainageIssue #Hyderabad",
                "upvotes": 98,
                "timestamp": "2026-03-26 10:00",
                "formal_letter": "To,\nThe Executive Engineer,\nGHMC Drainage Wing...",
                "status": "Unresolved"
            },
            {
                "id": 6,
                "user": "Deepa_Gachibowli",
                "avatar": "👩",
                "area": "Gachibowli",
                "city": "Hyderabad",
                "category": "Traffic Signal / Road Safety",
                "complaint": "Traffic signal at Gachibowli flyover junction not working for 10 days. Near miss accidents daily during peak hours. IT employees risking lives every morning.",
                "proof": "Photos of non-functional signal + near miss video",
                "duration": "1-2 weeks",
                "severity_score": 8,
                "severity_label": "Critical",
                "authority": "Hyderabad Traffic Police — Cyberabad Division",
                "categories": ["Traffic Safety", "Signal", "Cyberabad"],
                "hashtags": "#GachibowliTraffic #HyderabadPolice #RoadSafety #FixTheSignal",
                "upvotes": 211,
                "timestamp": "2026-03-26 08:30",
                "formal_letter": "To,\nThe DCP Traffic,\nCyberabad Division...",
                "status": "Unresolved"
            },
            {
                "id": 7,
                "user": "Ramesh_Kukatpally",
                "avatar": "🧑",
                "area": "Kukatpally",
                "city": "Hyderabad",
                "category": "Illegal Construction",
                "complaint": "Illegal construction blocking emergency vehicle access in Kukatpally Housing Board colony. Fire truck cannot enter. Serious safety risk for entire colony of 500 families.",
                "proof": "Measurement photos + colony layout showing blockage",
                "duration": "1 month",
                "severity_score": 7,
                "severity_label": "High",
                "authority": "GHMC Town Planning Wing",
                "categories": ["Illegal Construction", "Emergency Access", "GHMC"],
                "hashtags": "#KukatpallyConstruction #GHMC #IllegalBuilding #SafetyRisk",
                "upvotes": 87,
                "timestamp": "2026-03-25 16:15",
                "formal_letter": "To,\nThe Town Planning Officer,\nGHMC...",
                "status": "Unresolved"
            },
            {
                "id": 8,
                "user": "Sunita_Himayatnagar",
                "avatar": "👩",
                "area": "Himayatnagar",
                "city": "Hyderabad",
                "category": "Noise Pollution",
                "complaint": "Illegal bar playing loud music until 3am every night near residential area in Himayatnagar. Children cannot sleep. Elderly with heart conditions affected. Police not responding.",
                "proof": "Audio recordings + decibel meter readings + medical certificates",
                "duration": "2-3 months",
                "severity_score": 6,
                "severity_label": "High",
                "authority": "Hyderabad City Police — Himayatnagar Station",
                "categories": ["Noise Pollution", "Illegal Bar", "Police"],
                "hashtags": "#NoisePollution #HimayatnagarBar #HyderabadPolice #NightPeace",
                "upvotes": 73,
                "timestamp": "2026-03-25 22:00",
                "formal_letter": "To,\nThe Station House Officer,\nHimayatnagar Police Station...",
                "status": "Unresolved"
            },
            {
                "id": 9,
                "user": "Kiran_Secunderabad",
                "avatar": "🧑",
                "area": "Secunderabad",
                "city": "Hyderabad",
                "category": "Public Property Damage",
                "complaint": "Park benches and children play equipment completely broken in Secunderabad central park. Kids getting injured on sharp edges. Parents afraid to bring children. No maintenance for 8 months.",
                "proof": "Photos of broken equipment + child injury photos with parent permission",
                "duration": "6+ months",
                "severity_score": 6,
                "severity_label": "High",
                "authority": "GHMC Parks & Playgrounds Division",
                "categories": ["Child Safety", "Park Maintenance", "GHMC"],
                "hashtags": "#SecunderabadPark #ChildSafety #GHMC #BrokenPark",
                "upvotes": 64,
                "timestamp": "2026-03-24 15:30",
                "formal_letter": "To,\nThe Director,\nGHMC Parks Division...",
                "status": "Unresolved"
            },
            {
                "id": 10,
                "user": "Ananya_Banjara",
                "avatar": "👩",
                "area": "Banjara Hills",
                "city": "Hyderabad",
                "category": "Air / Water Pollution",
                "complaint": "Construction site near Road No 12 Banjara Hills dumping debris into storm water drain. Water turning black. Residents downstream reporting skin problems and contaminated borewell water.",
                "proof": "Water sample photos + lab test report + doctor certificates",
                "duration": "1 month",
                "severity_score": 8,
                "severity_label": "Critical",
                "authority": "Telangana Pollution Control Board",
                "categories": ["Water Pollution", "Construction Waste", "Health Risk"],
                "hashtags": "#BanjaraHillsPollution #WaterPollution #TSPCB #StopPollution",
                "upvotes": 142,
                "timestamp": "2026-03-24 11:00",
                "formal_letter": "To,\nThe Member Secretary,\nTelangana State Pollution Control Board...",
                "status": "Unresolved"
            }
        ]
        save_complaints(seed_data)

# ── AI Analysis ───────────────────────────────────────
def analyze_complaint_claude(api_key, city, area, category,
                              complaint_text, proof, duration,
                              previous, affected):
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""You are an expert civic complaint analyzer for Indian cities.

Analyze this complaint and respond ONLY with valid JSON:

City: {city}
Area: {area}
Problem: {category}
Description: {complaint_text}
Proof: {proof}
Duration: {duration}
Previously complained: {previous}
People affected: {affected}

Respond with ONLY this JSON structure, no other text:
{{
  "severity_score": <1-10>,
  "severity_label": "<Critical/High/Medium/Low>",
  "severity_reason": "<one sentence>",
  "primary_authority": "<department name>",
  "secondary_authority": "<escalation authority>",
  "categories": ["<tag1>", "<tag2>", "<tag3>"],
  "hashtags": "<4 hashtags as single string>",
  "estimated_resolution_days": <number>,
  "formal_complaint_letter": "<complete formal letter>",
  "whatsapp_message": "<short WhatsApp message>",
  "twitter_post": "<tweet under 280 chars>",
  "next_steps": ["<step1>", "<step2>", "<step3>"],
  "legal_rights": "<citizen legal right>"
}}

For formal_complaint_letter write a complete professional letter
with subject, date placeholder, body and signature placeholder.
JSON only, no other text."""

    response = model.generate_content(prompt)
    raw = response.text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())

# ── Complaint Card ────────────────────────────────────
def render_complaint_card(c, index):
    severity = c.get("severity_score", 5)
    label = c.get("severity_label", "Medium")

    if severity >= 8:
        badge = "🚨 CRITICAL"
        color = "#FF4444"
    elif severity >= 6:
        badge = "⚠️ HIGH"
        color = "#FF8C00"
    elif severity >= 4:
        badge = "🟡 MEDIUM"
        color = "#FFD700"
    else:
        badge = "🔵 LOW"
        color = "#4169E1"

    with st.container():
        st.markdown(f"""
        <div style='
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 16px;
            background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        '>
            <div style='display:flex; 
                        justify-content:space-between; 
                        align-items:center; 
                        margin-bottom:8px'>
                <span style='font-weight:bold; font-size:15px'>
                    {c.get('avatar','🧑')} @{c.get('user','Anonymous')}
                </span>
                <span style='
                    background:{color};
                    color:white;
                    padding:3px 10px;
                    border-radius:20px;
                    font-size:12px;
                    font-weight:bold
                '>{badge}</span>
            </div>
            <div style='color:#666; 
                        font-size:12px; 
                        margin-bottom:8px'>
                📍 {c.get('area','')}, {c.get('city','')} &nbsp;|&nbsp; 
                🕐 {c.get('timestamp','')} &nbsp;|&nbsp; 
                📂 {c.get('category','')}
            </div>
            <p style='margin:8px 0; 
                      font-size:14px; 
                      line-height:1.5'>
                {c.get('complaint','')}
            </p>
            <div style='color:#888; font-size:12px; margin:6px 0'>
                📎 Proof: {c.get('proof','')}
            </div>
            <div style='color:#1A4A8A; 
                        font-size:12px; 
                        margin:6px 0'>
                🏛️ {c.get('authority','')}
            </div>
            <div style='color:#666; 
                        font-size:12px; 
                        margin:6px 0'>
                {c.get('hashtags','')}
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            upvotes = c.get("upvotes", 0)
            if st.button(f"👆 {upvotes} Upvotes",
                         key=f"upvote_{c['id']}_{index}"):
                complaints = load_complaints()
                for comp in complaints:
                    if comp["id"] == c["id"]:
                        comp["upvotes"] = comp.get("upvotes", 0) + 1
                        break
                save_complaints(complaints)
                st.rerun()

        with col2:
            if st.button("📄 View Letter",
                         key=f"letter_{c['id']}_{index}"):
                st.session_state[f"show_letter_{c['id']}"] = \
                    not st.session_state.get(
                        f"show_letter_{c['id']}", False)

        with col3:
            status = c.get("status", "Unresolved")
            if status == "Resolved":
                st.success("✅ Resolved")
            else:
                st.error("❌ Unresolved")

        if st.session_state.get(f"show_letter_{c['id']}", False):
            st.text_area(
                "Formal Complaint Letter:",
                c.get("formal_letter", "Letter not available"),
                height=200,
                key=f"lettertext_{c['id']}_{index}"
            )

        st.markdown("---")

# ── Main App ──────────────────────────────────────────
def main():
    initialize_db()

    # Sidebar
    with st.sidebar:
        st.markdown("## 📢 ComplaintGram")
        st.markdown("*Instagram for civic complaints*")
        st.divider()

        api_key = st.text_input(
        "Gemini API Key",
            type="password",
            placeholder="sk-ant-..."
        )

        st.divider()
        st.markdown("### 🔍 Filter Feed")

        city_filter = st.selectbox(
            "City",
            ["All", "Hyderabad", "Mumbai",
             "Delhi", "Bengaluru", "Chennai"]
        )

        category_filter = st.selectbox(
            "Category",
            ["All", "Road / Pothole / Footpath",
             "Water Supply / Pipeline",
             "Electricity / Street Light",
             "Garbage / Sanitation",
             "Drainage / Flooding",
             "Traffic Signal / Road Safety",
             "Public Property Damage",
             "Noise Pollution",
             "Air / Water Pollution",
             "Illegal Construction"]
        )

        sort_by = st.selectbox(
            "Sort By",
            ["Most Upvoted", "Most Recent", "Most Critical"]
        )

        st.divider()
        complaints = load_complaints()
        total = len(complaints)
        critical = len([c for c in complaints
                       if c.get("severity_score", 0) >= 8])
        total_upvotes = sum(c.get("upvotes", 0)
                           for c in complaints)

        st.markdown("### 📊 Live Stats")
        st.metric("Total Complaints", total)
        st.metric("Critical Issues", critical)
        st.metric("Community Upvotes", total_upvotes)

        st.divider()
        st.markdown("### 🏆 Most Active Areas")
        areas = {}
        for c in complaints:
            area = c.get("area", "Unknown")
            areas[area] = areas.get(area, 0) + 1
        for area, count in sorted(areas.items(),
                                   key=lambda x: x[1],
                                   reverse=True)[:5]:
            st.markdown(f"📍 **{area}** — {count} complaints")

    # Main content
    tab1, tab2 = st.tabs(["📰 Feed", "➕ Post Complaint"])

    # ── FEED TAB ──────────────────────────────────────
    with tab1:
        st.markdown("""
        <h2 style='color:#1A4A8A'>
            📢 ComplaintGram Feed
        </h2>
        <p style='color:gray'>
            Real complaints. Real proof. Real pressure.
        </p>
        """, unsafe_allow_html=True)

        complaints = load_complaints()

        # Filter
        if city_filter != "All":
            complaints = [c for c in complaints
                         if c.get("city") == city_filter]
        if category_filter != "All":
            complaints = [c for c in complaints
                         if c.get("category") == category_filter]

        # Sort
        if sort_by == "Most Upvoted":
            complaints.sort(
                key=lambda x: x.get("upvotes", 0),
                reverse=True)
        elif sort_by == "Most Recent":
            complaints.sort(
                key=lambda x: x.get("timestamp", ""),
                reverse=True)
        elif sort_by == "Most Critical":
            complaints.sort(
                key=lambda x: x.get("severity_score", 0),
                reverse=True)

        if not complaints:
            st.info("No complaints found for selected filters.")
        else:
            st.markdown(
                f"**{len(complaints)} complaints found**")
            for i, complaint in enumerate(complaints):
                render_complaint_card(complaint, i)

    # ── POST TAB ──────────────────────────────────────
    with tab2:
        st.markdown("""
        <h2 style='color:#1A4A8A'>
            ➕ Post a Complaint
        </h2>
        <p style='color:gray'>
            AI will analyze, route to right authority 
            and generate your formal letter instantly.
        </p>
        """, unsafe_allow_html=True)

        if not api_key:
            st.warning(
                "Enter your Claude API key in the sidebar "
                "to post complaints with AI analysis.")

        your_name = st.text_input(
            "Your Username",
            placeholder="e.g. Ravi_Hyderabad"
        )

        col1, col2 = st.columns(2)
        with col1:
            city = st.selectbox("City", [
                "Hyderabad", "Mumbai", "Delhi",
                "Bengaluru", "Chennai", "Kolkata",
                "Pune", "Other"
            ], key="post_city")
        with col2:
            area = st.text_input(
                "Area / Locality",
                placeholder="e.g. Miyapur"
            )

        category = st.selectbox("Problem Type", [
            "Road / Pothole / Footpath",
            "Water Supply / Pipeline",
            "Electricity / Street Light",
            "Garbage / Sanitation",
            "Drainage / Flooding",
            "Traffic Signal / Road Safety",
            "Public Property Damage",
            "Noise Pollution",
            "Air / Water Pollution",
            "Illegal Construction",
            "Other"
        ], key="post_category")

        complaint_text = st.text_area(
            "Describe your complaint",
            height=150,
            placeholder="Be specific — location, duration, impact"
        )

        proof = st.text_area(
            "Describe your proof",
            height=80,
            placeholder="Photos, videos, receipts you have"
        )

        col3, col4 = st.columns(2)
        with col3:
            duration = st.selectbox("How long?", [
                "Just noticed", "Few days", "1-2 weeks",
                "1 month", "2-3 months",
                "6+ months", "Over a year"
            ])
        with col4:
            affected = st.selectbox("People affected?", [
                "Just me", "10-50 people",
                "50-200 people", "200-1000 people",
                "Entire locality / thousands"
            ])

        previous = st.checkbox("Complained before with no response")

        if st.button("🚀 Post & Analyze",
                     type="primary",
                     use_container_width=True):
            if not complaint_text:
                st.error("Please describe your complaint.")
            elif not area:
                st.error("Please enter your area.")
            elif not your_name:
                st.error("Please enter your username.")
            elif not api_key:
                st.error("Please enter Claude API key in sidebar.")
            else:
                with st.spinner(
                    "AI analyzing your complaint..."):
                    try:
                        data = analyze_complaint_claude(
                            api_key, city, area, category,
                            complaint_text, proof, duration,
                            previous, affected
                        )

                        complaints = load_complaints()
                        new_id = max(
                            [c["id"] for c in complaints],
                            default=0) + 1

                        avatars = ["🧑", "👨", "👩",
                                   "🧔", "👱", "🧑‍💻"]
                        new_complaint = {
                            "id": new_id,
                            "user": your_name,
                            "avatar": random.choice(avatars),
                            "area": area,
                            "city": city,
                            "category": category,
                            "complaint": complaint_text,
                            "proof": proof,
                            "duration": duration,
                            "severity_score": data.get(
                                "severity_score", 5),
                            "severity_label": data.get(
                                "severity_label", "Medium"),
                            "authority": data.get(
                                "primary_authority", ""),
                            "categories": data.get(
                                "categories", []),
                            "hashtags": data.get(
                                "hashtags", ""),
                            "upvotes": 1,
                            "timestamp": datetime.now().strftime(
                                "%Y-%m-%d %H:%M"),
                            "formal_letter": data.get(
                                "formal_complaint_letter", ""),
                            "whatsapp_message": data.get(
                                "whatsapp_message", ""),
                            "twitter_post": data.get(
                                "twitter_post", ""),
                            "next_steps": data.get(
                                "next_steps", []),
                            "legal_rights": data.get(
                                "legal_rights", ""),
                            "status": "Unresolved"
                        }

                        complaints.insert(0, new_complaint)
                        save_complaints(complaints)

                        st.success(
                            "Complaint posted successfully!")
                        st.balloons()

                        # Show AI analysis
                        st.divider()
                        st.subheader("🤖 AI Analysis")

                        severity = data.get(
                            "severity_score", 5)
                        if severity >= 8:
                            st.error(
                                f"🚨 Severity: {severity}/10 "
                                f"— {data.get('severity_label')}")
                        elif severity >= 6:
                            st.warning(
                                f"⚠️ Severity: {severity}/10 "
                                f"— {data.get('severity_label')}")
                        else:
                            st.info(
                                f"Severity: {severity}/10 "
                                f"— {data.get('severity_label')}")

                        st.markdown(
                            f"**File with:** "
                            f"{data.get('primary_authority')}")
                        st.markdown(
                            f"**Escalate to:** "
                            f"{data.get('secondary_authority')}")
                        st.markdown(
                            f"**Your legal right:** "
                            f"{data.get('legal_rights')}")

                        st.subheader("📄 Your Formal Letter")
                        st.text_area(
                            "Ready to print and submit:",
                            data.get(
                                "formal_complaint_letter", ""),
                            height=300
                        )
                        st.download_button(
                            "📥 Download Letter",
                            data.get(
                                "formal_complaint_letter", ""),
                            file_name="complaint_letter.txt"
                        )

                        st.subheader("📱 Share to Create Pressure")
                        t1, t2 = st.tabs(["Tweet", "WhatsApp"])
                        with t1:
                            st.text_area(
                                "Tweet:",
                                data.get("twitter_post", ""),
                                height=80
                            )
                        with t2:
                            st.text_area(
                                "WhatsApp:",
                                data.get("whatsapp_message", ""),
                                height=100
                            )

                    except Exception as e:
                        st.error(f"Error: {str(e)}")

    st.divider()
    st.caption(
        "ComplaintGram — Built by Yoshitha Dhannapuneni | "
        "AI-powered civic accountability for India | "
        "Powered by Claude AI"
    )

if __name__ == "__main__":
    main()
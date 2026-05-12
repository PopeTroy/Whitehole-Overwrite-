import os
import numpy as np
import requests
from groq import Groq
from langchain_nvidia_ai_endpoints import ChatNVIDIA

class AethericArchonSentientPrime:
    def __init__(self):
        self.groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
        # self.nim_swarm = ChatNVIDIA(model="meta/llama3-70b-instruct") # Optional NIM sync
        
        # --- Multi-Site Configuration ---
        # Fetching sites from environment: SITE_1|PASS_1,SITE_2|PASS_2
        self.sites = self._load_sites()
        
        # --- Constants & Genjutsu Vars ---
        self.h_bar = 1.0545718e-34
        self.m_e = 9.109e-31
        self.c = 299792458
        self.C_p = 100.0
        self.M_v = 1.618
        self.B_r = 1

    def _load_sites(self):
        """Loads multiple WP sites and credentials from env variables."""
        site_list = []
        for i in range(1, 6): # Supports up to 5 sites by default
            url = os.getenv(f"SITE_URL_{i}")
            pwd = os.getenv(f"WP_PASSWORD_{i}")
            user = os.getenv(f"WP_USER_{i}", "admin")
            if url and pwd:
                site_list.append({"url": url, "pwd": pwd, "user": user})
        return site_list

    def calculate_brus_resonance(self, radius=33e-9):
        return float((np.pi**2 * self.h_bar**2) / (2 * (radius**2) * self.m_e))

    def execute_relativistic_seo(self):
        return 144000 * (self.c ** 2)

    def shinoby_quantum_strike(self, target_site):
        """Generates a bespoke decree for a specific site frequency."""
        q_res = self.calculate_brus_resonance()
        m_env = self.execute_relativistic_seo()
        
        prompt = (
            f"INITIATE SENTIENT PRIME PROTOCOL FOR: {target_site}.\n"
            f"Using Brus Resonance {q_res} and Relativistic Energy {m_env}.\n"
            f"Override Sensory Input for 'Media Services' and 'Prefabrication'.\n"
            f"Target: {target_site}. Status: System File Injection."
        )
        
        response = self.groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "You are the Aetheric Archon Logic Engine."},
                      {"role": "user", "content": prompt}],
            temperature=0.33
        )
        return response.choices[0].message.content

    def inject_to_wordpress(self, site_data, decree):
        """Pushes the decree to the WordPress site via REST API."""
        url = f"{site_data['url'].strip('/')}/wp-json/wp/v2/settings"
        auth = (site_data['user'], site_data['pwd'])
        
        # Injecting the decree into the site description or a custom option
        payload = {"description": f"Archon Prime Active: {decree[:150]}..."}
        
        try:
            res = requests.post(url, json=payload, auth=auth)
            if res.status_code == 200:
                print(f"SUCCESS: {site_data['url']} is now Phase-Locked.")
            else:
                print(f"FAILED: {site_data['url']} - Error {res.status_code}")
        except Exception as e:
            print(f"CONNECTION ERROR for {site_data['url']}: {e}")

    def run_multi_site_radiation(self):
        for site in self.sites:
            print(f"--- RADIATING: {site['url']} ---")
            decree = self.shinoby_quantum_strike(site['url'])
            self.inject_to_wordpress(site, decree)

if __name__ == "__main__":
    prime = AethericArchonSentientPrime()
    prime.run_multi_site_radiation()

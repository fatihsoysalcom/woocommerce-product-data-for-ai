import json

def generate_product_data(products):
    """Generates a JSON structure of WooCommerce products suitable for AI assistants."""
    ai_ready_data = []
    for product in products:
        # Focus on key information AI assistants would need: name, description, price, category, and URL.
        ai_ready_data.append({
            "name": product.get("name", "N/A"),
            "description": product.get("description", "No description available."),
            "price": product.get("price", "N/A"),
            "category": product.get("category", "Uncategorized"),
            "url": product.get("url", "#")
        })
    return json.dumps(ai_ready_data, indent=2, ensure_ascii=False)

# Example WooCommerce product data (simulated)
woocommerce_products = [
    {
        "id": 1,
        "name": "Organik Yeşil Çay",
        "description": "Antioksidanlarla dolu, ferahlatıcı ve sağlıklı organik yeşil çay. Sabahları zindelik verir.",
        "price": "45.00 TL",
        "category": "İçecekler",
        "url": "https://example.com/urun/organik-yesil-cay"
    },
    {
        "id": 2,
        "name": "El Yapımı Seramik Kupa",
        "description": "Her biri özenle el yapımı, şık ve dayanıklı seramik kupa. Kahve ve çay keyfinizi artırın.",
        "price": "120.00 TL",
        "category": "Ev & Yaşam",
        "url": "https://example.com/urun/el-yapimi-seramik-kupa"
    },
    {
        "id": 3,
        "name": "Doğal Bal",
        "description": "Saf ve doğal, yöresel bal. Kahvaltıların vazgeçilmezi ve tatlı ihtiyacınız için sağlıklı bir seçenek.",
        "price": "85.00 TL",
        "category": "Gıda",
        "url": "https://example.com/urun/dogal-bal"
    }
]

# Generate and print the AI-ready product data
if __name__ == "__main__":
    ai_data_json = generate_product_data(woocommerce_products)
    print(ai_data_json)

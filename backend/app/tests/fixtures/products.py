"""
@pytest.fixture(scope="module")
def populate_products() -> ProductOutSchema:
    return ProductOutSchema(
        source="ff 21*297",
        translation="format ferme 210 x 297 mm",
    )
"""

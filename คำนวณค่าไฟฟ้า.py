# สถานีผลิตไฟฟ้าอำเภอเชียงคาน
# 6623540132 พันตำรวจโทวิศิษฎ์ ทองโม้
# 
# 
# 

def calculate_electric_bill(unit):
    total_cost = 0
    service_charge = 8.19

    if unit > 400:
        total_cost += 15 * 2.3488
        total_cost += 10 * 2.9882
        total_cost += 10 * 3.2405
        total_cost += 65 * 3.6237
        total_cost += 50 * 3.7171
        total_cost += 250 * 4.2218
        left_unit = unit - 400
        total_cost += left_unit * 4.4217

    elif unit >= 151 and unit <= 400:
        total_cost += 15 * 2.3488
        total_cost += 10 * 2.9882
        total_cost += 10 * 3.2405
        total_cost += 65 * 3.6237
        total_cost += 50 * 3.7171
        left_unit = unit - 150
        total_cost += left_unit * 4.2218

    elif unit >= 101 and unit <= 150:
        total_cost += 15 * 2.3488
        total_cost += 10 * 2.9882
        total_cost += 10 * 3.2405
        total_cost += 65 * 3.6237
        left_unit = unit - 100
        total_cost += left_unit * 3.7171

    elif unit >= 36 and unit <= 100:
        total_cost += 15 * 2.3488
        total_cost += 10 * 2.9882
        total_cost += 10 * 3.2405
        left_unit = unit - 35
        total_cost += left_unit * 3.6237

    elif unit >= 26 and unit <= 35:
        total_cost += 15 * 2.3488
        total_cost += 10 * 2.9882
        left_unit = unit - 25
        total_cost += left_unit * 3.2405

    elif unit >= 16 and unit <= 25:
        total_cost += 15 * 2.3488
        left_unit = unit - 15
        total_cost += left_unit * 2.9882
    
    elif unit >= 1 and unit <= 15:
        total_cost += unit * 2.9882

    total_cost += service_charge
    print(total_cost)

calculate_electric_bill(25)

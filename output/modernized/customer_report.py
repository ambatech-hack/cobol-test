import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CustomerRecord:
    cust_id: int
    cust_name: str
    cust_region: str
    sales_amount: float
    payment_status: str

    def __post_init__(self):
        if self.payment_status not in ('P', 'N'):
            raise ValueError("Invalid payment status")


def read_customer_file(filename: str) -> list[CustomerRecord]:
        # 
    records = []
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            try:
                record = CustomerRecord(*row)
            except ValueError as e:
                print(f"Error reading customer record: {e}")
                continue
            records.append(record)
    return records


def write_report_header(writer):
        # The function name is WRITE-REPORT-HEADER, it has a complexity of 10, no parameters, and it returns nothing (void).
    writer.writerow(["ID", "NAME", "REGION", "SALES", "STATUS"])


def process_customers(records):
        # 
    total_customers = 0
    paid_count = 0
    pending_count = 0
    total_sales = 0
    paid_sales = 0
    pending_sales = 0
    north_total = 0
    south_total = 0
    east_total = 0
    west_total = 0
    commission = 0.0
    high_value_limit = 50000.0

    for record in records:
        total_customers += 1
        total_sales += record.sales_amount

        if record.payment_status == 'P':
            paid_count += 1
            paid_sales += record.sales_amount
        elif record.payment_status == 'N':
            pending_count += 1
            pending_sales += record.sales_amount

        region_totals = {
            'north': north_total,
            'south': south_total,
            'east': east_total,
            'west': west_total,
        }
        region_totals[record.cust_region] += record.sales_amount

        if record.sales_amount > high_value_limit:
            commission += record.sales_amount * 0.075 * 1.5
        else:
            commission += record.sales_amount * 0.075

    return {
        'total_customers': total_customers,
        'paid_count': paid_count,
        'pending_count': pending_count,
        'total_sales': total_sales,
        'paid_sales': paid_sales,
        'pending_sales': pending_sales,
        'north_total': north_total,
        'south_total': south_total,
        'east_total': east_total,
        'west_total': west_total,
        'commission': commission,
    }


def generate_summary(summary):
        # 
    print("=" * 40)
    print("MONTHLY CUSTOMER SALES REPORT".center(40))
    print("-" * 40)
    print(f"{'ID':<5} {'NAME':<30} {'REGION':<10} {'SALES':>9} {'STATUS':<7}".center(40))
    print("-" * 40)
    print(f"{summary['total_customers']:<5} {summary['total_sales']:>9.2f}".center(40))
    print("-" * 40)
    print(f"{'PAID':<5} {summary['paid_sales']:>9.2f}".center(40))
    print(f"{'PENDING':<5} {summary['pending_sales']:>9.2f}".center(40))
    print("-" * 40)
    print(f"{'NORTH':<5} {summary['north_total']:>9.2f}".center(40))
    print(f"{'SOUTH':<5} {summary['south_total']:>9.2f}".center(40))
    print(f"{'EAST':<5} {summary['east_total']:>9.2f}".center(40))
    print(f"{'WEST':<5} {summary['west_total']:>9.2f}".center(40))
    print("-" * 40)
    print(f"{'PAID ACCOUNTS':<5} {summary['paid_count']:>9}".center(40))
    print(f"{'PAID SALES TOTAL':<5} {summary['paid_sales']:>9.2f}".center(40))
    print(f"{'PENDING ACCOUNTS':<5} {summary['pending_count']:>9}".center(40))
    print(f"{'PENDING SALES TOTAL':<5} {summary['pending_sales']:>9.2f}".center(40))
    print("-" * 40)
    print(f"{'TOTAL COMMISSION':<5} {summary['commission']:>9.2f}".center(40))
    print("=" * 40)


if __name__ == "__main__":
    filename = "custdata.dat"
    records = read_customer_file(filename)
    summary = process_customers(records)
    report_path = Path("salesrpt.txt")
    with open(report_path, "w", newline="") as file:
        writer = csv.writer(file)
        write_report_header(writer)
        for record in records:
            writer.writerow([
                record.cust_id,
                record.cust_name,
                record.cust_region,
                record.sales_amount,
                record.payment_status,
            ])
    generate_summary(summary)
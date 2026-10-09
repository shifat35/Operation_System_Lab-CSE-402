def fcfs(requests, head):
    """Serve requests in the order they arrive."""
    order = [head]
    movement = 0
    current = head

    for r in requests:
        movement += abs(current - r)
        current = r
        order.append(r)

    return order, movement


def sstf(requests, head):
    """Always serve the pending request closest to the current head."""
    order = [head]
    movement = 0
    current = head
    pending = requests.copy()

    while pending:
        nearest = min(pending, key=lambda r: abs(current - r))
        pending.remove(nearest)

        movement += abs(current - nearest)
        current = nearest
        order.append(nearest)

    return order, movement


def show_result(name, order, movement):
    print(f"\n{'=' * 10} {name} {'=' * 10}")
    print("Seek Order:", " -> ".join(map(str, order)))
    print("Total Head Movement =", movement)


def compare(fcfs_move, sstf_move):
    print(f"\n{'=' * 10} COMPARISON {'=' * 10}")
    print("FCFS Total Head Movement =", fcfs_move)
    print("SSTF Total Head Movement =", sstf_move)

    diff = abs(fcfs_move - sstf_move)

    if sstf_move < fcfs_move:
        print("\nSSTF is better than FCFS.")
        print(f"SSTF has less head movement by {diff} cylinders.")
    elif fcfs_move < sstf_move:
        print("\nFCFS is better than SSTF.")
        print(f"FCFS has less head movement by {diff} cylinders.")
    else:
        print("\nBoth SSTF and FCFS have the same head movement.")


def main():
    requests = [3, 60, 10, 25, 30, 4]
    head = 41

    sstf_order, sstf_move = sstf(requests, head)
    fcfs_order, fcfs_move = fcfs(requests, head)

    show_result("SSTF", sstf_order, sstf_move)
    show_result("FCFS", fcfs_order, fcfs_move)
    compare(fcfs_move, sstf_move)


if __name__ == "__main__":
    main()

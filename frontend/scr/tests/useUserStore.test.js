import { act, renderHook } from "@testing-library/react-hooks";
import { useUserStore } from "../store/useUserStore";

global.fetch = jest.fn();

describe("useUserStore", () => {
  beforeEach(() => {
    fetch.mockClear();
  });

  test("fetchUsers sets users on success", async () => {
    const fakeUsers = [{ id: 1, name: "Mario" }];
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => fakeUsers,
    });

    const { result } = renderHook(() => useUserStore());

    await act(async () => {
      await result.current.fetchUsers();
    });

    expect(result.current.users).toEqual(fakeUsers);
    expect(result.current.loading).toBe(false);
    expect(result.current.error).toBeNull();
  });

  test("fetchUsers sets error on failure", async () => {
    fetch.mockResolvedValueOnce({ ok: false });

    const { result } = renderHook(() => useUserStore());

    await act(async () => {
      await result.current.fetchUsers();
    });

    expect(result.current.error).not.toBeNull();
    expect(result.current.loading).toBe(false);
  });
});

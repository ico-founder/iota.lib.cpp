//
// MIT License
//
// Copyright (c) 2017-2018 Thibault Martinez and Simon Ninon
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//
//

#pragma once

#include <iota/api/responses/base.hpp>
#include <iota/models/fwd.hpp>

namespace IOTA {

namespace API {

namespace Responses {

/**
 * GetTransfer API call response.
 * Returns the transfers which are associated with a seed. The transfers are determined by either
 * calculating deterministically which addresses were already used, or by providing a list of
 * indexes to get the transfers from.
 */
class GetTransfers : public Base {
public:
  /**
   * Default ctor.
   */
  GetTransfers() = default;

  /**
   * Full init ctor.
   *
   * @param transferBundle The transfer bundle.
   * @param duration Request duration.
   */
  GetTransfers(const std::vector<Models::Bundle>& transferBundle, const int64_t& duration);

  /**
   * Default dtor.
   */
  ~GetTransfers() = default;

public:
  /**
   * @return The transfers.
   */
  const std::vector<Models::Bundle>& getTransfers() const;

  /**
   * @return The transfers (non const version).
   */
  std::vector<Models::Bundle>& getTransfers();

  /**
   * @param transfers New vector of transfers for GetTransfers.
   */
  void setTransfers(const std::vector<Models::Bundle>& transfers);

private:
  std::vector<Models::Bundle> transferBundle_;
};

}  // namespace Responses

}  // namespace API

}  // namespace IOTA

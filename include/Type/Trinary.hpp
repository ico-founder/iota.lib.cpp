//
// MIT License
//
// Copyright (c) 2017 Thibault Martinez
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

#include <cstdint>
#include <iostream>
#include <vector>

namespace IOTA {

namespace Type {

typedef std::vector<int8_t> Trits;
typedef std::string         Trytes;

bool isValidTryte(const char& tryte);

std::vector<int8_t> tritsToBytes(const Trits& trits);
Trits               bytesToTrits(const std::vector<int8_t>& bytes);

Trits  trytesToTrits(const Trytes& trytes);
Trytes tritsToTrytes(const Trits& trits);
Trytes tritsToTrytes(const Trits& trits, unsigned int length);

Type::Trits intToTrits(const int& value);
template <typename T>
T
tritsToInt(const Trits& trits) {
  T res = 0;

  for (int i = trits.size() - 1; i >= 0; --i) {
    res = res * 3 + trits[i];
  }

  return res;
}

}  // namespace Type

}  // namespace IOTA
